"""Main entry point for bank statement processor."""

import sys
from database import DatabaseManager
from file_manager import FileManager
from statement_processor import StatementProcessor
from report_generator import ReportGenerator


def main():
    """Main execution function."""
    # Initialize database
    db_manager = DatabaseManager()
    
    # Fetch categories from MongoDB
    categories = db_manager.fetch_categories()
    
    # Print categories if flag is provided
    if '--print-categories' in sys.argv:
        db_manager.print_categories(categories)
    
    # Build alias mapping
    alias_to_category = db_manager.build_alias_map(categories)
    
    # Read and prepare bank statement
    bank_statement = FileManager.read_bank_statement('bank_statement.xls', skiprows=22)
    bank_statement = FileManager.prepare_statement(bank_statement)
    
    # Process statement by month
    processor = StatementProcessor(categories, alias_to_category)
    monthly_spending, unprocessed_rows, row_stats = processor.process_monthly_statements(bank_statement)
    
    # Generate and display report
    ReportGenerator.generate_report(bank_statement, monthly_spending, unprocessed_rows, row_stats)


if __name__ == '__main__':
    main()
