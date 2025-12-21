"""Statement processing logic for bank statement processor."""


class StatementProcessor:
    """Processes bank statement transactions."""
    
    def __init__(self, categories, alias_to_category):
        """
        Initialize processor.
        
        Args:
            categories: List of category dictionaries
            alias_to_category: Dictionary mapping aliases to category names
        """
        self.categories = categories
        self.alias_to_category = alias_to_category
    
    def process_monthly_statements(self, bank_statement):
        """
        Process bank statement grouped by month.
        
        Args:
            bank_statement: Prepared DataFrame with month column
            
        Returns:
            Tuple of (monthly_spending, unprocessed_rows)
        """
        monthly_groups = bank_statement.groupby('month')
        monthly_spending = {}
        unprocessed_rows = []
        
        for month, group in monthly_groups:
            spending_summary = self._process_month(month, group, unprocessed_rows)
            monthly_spending[str(month)] = spending_summary
        
        return monthly_spending, unprocessed_rows
    
    def _process_month(self, month, group, unprocessed_rows):
        """
        Process transactions for a single month.
        
        Args:
            month: Month period
            group: DataFrame rows for this month
            unprocessed_rows: List to track unprocessed rows
            
        Returns:
            Spending summary dictionary for the month
        """
        spending_summary = {category['name']: 0 for category in self.categories}
        
        for index, row in group.iterrows():
            self._process_transaction(index, row, spending_summary, month, unprocessed_rows)
        
        return spending_summary
    
    def _process_transaction(self, index, row, spending_summary, month, unprocessed_rows):
        """
        Process a single transaction.
        
        Args:
            index: Row index
            row: Row data
            spending_summary: Dictionary to accumulate spending
            month: Month period for tracking
            unprocessed_rows: List to track unprocessed rows
        """
        description = str(row.iloc[1]).lower()  # 2nd column
        debit_amount = row.iloc[4]  # 5th column
        credit_amount = row.iloc[5]  # 6th column
        
        # Skip if description is empty or NaN
        if description == 'nan' or not description.strip():
            unprocessed_rows.append({
                'month': str(month),
                'row_num': index + 23,
                'reason': 'Empty or NaN description'
            })
            return
        
        # Skip if there's no debit but there is credit (income/credit transactions)
        import pandas as pd
        if (pd.isna(debit_amount) or debit_amount == 0) and pd.notna(credit_amount) and credit_amount > 0:
            unprocessed_rows.append({
                'month': str(month),
                'row_num': index + 23,
                'reason': 'Credit transaction (no debit)',
                'description': description,
                'credit': credit_amount
            })
            return
        
        # Find matching category
        found_category = False
        for alias, category_name in self.alias_to_category.items():
            if alias in description:
                spending_summary[category_name] += debit_amount
                found_category = True
                break
        
        # Track rows that didn't match any category
        if not found_category:
            unprocessed_rows.append({
                'month': str(month),
                'row_num': index + 23,
                'reason': 'No matching category',
                'description': description,
                'debit': debit_amount
            })
