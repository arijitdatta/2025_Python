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
            Tuple of (monthly_spending, unprocessed_rows, row_stats)
        """
        monthly_groups = bank_statement.groupby('month')
        monthly_spending = {}
        unprocessed_rows = []
        row_stats = {
            'total_debit_rows': 0,
            'total_credit_rows': 0,
            'monthly_debit': {},
            'monthly_credit': {}
        }
        
        for month, group in monthly_groups:
            spending_summary = self._process_month(month, group, unprocessed_rows, row_stats)
            monthly_spending[str(month)] = spending_summary
        
        return monthly_spending, unprocessed_rows, row_stats
    
    def _process_month(self, month, group, unprocessed_rows, row_stats):
        """
        Process transactions for a single month.
        
        Args:
            month: Month period
            group: DataFrame rows for this month
            unprocessed_rows: List to track unprocessed rows
            row_stats: Dictionary to track debit/credit statistics
            
        Returns:
            Spending summary dictionary for the month
        """
        spending_summary = {category['name']: 0 for category in self.categories}
        month_str = str(month)
        month_debit_count = 0
        month_credit_count = 0
        
        for index, row in group.iterrows():
            is_debit = self._process_transaction(index, row, spending_summary, month, unprocessed_rows)
            if is_debit == 'debit':
                month_debit_count += 1
            elif is_debit == 'credit':
                month_credit_count += 1
        
        row_stats['monthly_debit'][month_str] = month_debit_count
        row_stats['monthly_credit'][month_str] = month_credit_count
        row_stats['total_debit_rows'] += month_debit_count
        row_stats['total_credit_rows'] += month_credit_count
        
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
            
        Returns:
            'debit', 'credit', or None based on transaction type processed
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
            return None
        
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
            return 'credit'
        
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
            return None
        
        return 'debit'
