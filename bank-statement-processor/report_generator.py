"""Report generation for bank statement processor."""


class ReportGenerator:
    """Generates formatted reports for bank statement analysis."""
    
    @staticmethod
    def generate_report(bank_statement, monthly_spending, unprocessed_rows):
        """
        Generate and print complete analysis report.
        
        Args:
            bank_statement: Processed DataFrame
            monthly_spending: Dictionary of monthly spending by category
            unprocessed_rows: List of unprocessed transaction rows
        """
        ReportGenerator._print_header()
        ReportGenerator._print_statistics(bank_statement, unprocessed_rows)
        ReportGenerator._print_monthly_summary(monthly_spending)
        ReportGenerator._print_unprocessed_rows(unprocessed_rows)
        ReportGenerator._print_footer()
    
    @staticmethod
    def _print_header():
        """Print report header."""
        print("\n" + "="*60)
        print("BANK STATEMENT ANALYSIS REPORT")
        print("="*60)
    
    @staticmethod
    def _print_statistics(bank_statement, unprocessed_rows):
        """Print overall statistics."""
        total_rows = len(bank_statement)
        total_unprocessed = len(unprocessed_rows)
        total_processed = total_rows - total_unprocessed
        
        print(f"\n{'Overall Statistics':^60}")
        print("-"*60)
        print(f"Total Rows:          {total_rows:>5}")
        print(f"Processed Rows:      {total_processed:>5}")
        print(f"Unprocessed Rows:    {total_unprocessed:>5}")
        print("-"*60)
    
    @staticmethod
    def _print_monthly_summary(monthly_spending):
        """Print spending summary by month."""
        print(f"\n{'Monthly Spending Summary':^60}")
        print("-"*60)
        for month in sorted(monthly_spending.keys()):
            print(f"\n{month}")
            print("-"*60)
            for category, amount in monthly_spending[month].items():
                if amount > 0:  # Only print categories with spending
                    print(f"{category:<40} Rs{amount:>15.2f}")
        print("-"*60)
    
    @staticmethod
    def _print_unprocessed_rows(unprocessed_rows):
        """Print unprocessed rows."""
        if unprocessed_rows:
            print(f"\n{'Unprocessed Rows':^60}")
            print("-"*60)
            current_month = None
            for row_info in unprocessed_rows:
                if row_info['month'] != current_month:
                    current_month = row_info['month']
                    print(f"\n{current_month}")
                print(f"  Row {row_info['row_num']}: {row_info['reason']}")
                if 'description' in row_info:
                    if 'debit' in row_info:
                        print(f"    Description: {row_info['description']}, Debit: Rs{row_info['debit']:.2f}")
                    elif 'credit' in row_info:
                        print(f"    Description: {row_info['description']}, Credit: Rs{row_info['credit']:.2f}")
            print("-"*60)
        else:
            print(f"\n{'SUCCESS':^60}")
            print("-"*60)
            print("All rows processed successfully!")
            print("-"*60)
    
    @staticmethod
    def _print_footer():
        """Print report footer."""
        print("="*60)
