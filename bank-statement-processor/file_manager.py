"""File handling operations for bank statement processor."""

import os
import pandas as pd


class FileManager:
    """Manages file operations for bank statements."""
    
    @staticmethod
    def get_script_directory():
        """Get the directory where the script is located."""
        return os.path.dirname(os.path.abspath(__file__))
    
    @staticmethod
    def get_file_path(filename):
        """
        Get full file path relative to script directory.
        
        Args:
            filename: Relative filename
            
        Returns:
            Full path to the file
        """
        script_dir = FileManager.get_script_directory()
        return os.path.join(script_dir, filename)
    
    @staticmethod
    def file_exists(filename):
        """Check if file exists."""
        filepath = FileManager.get_file_path(filename)
        return os.path.exists(filepath)
    
    @staticmethod
    def read_bank_statement(filename, skiprows=22):
        """
        Read bank statement from XLS file.
        
        Args:
            filename: Path to XLS file (relative to script directory)
            skiprows: Number of rows to skip
            
        Returns:
            DataFrame containing bank statement
        """
        filepath = FileManager.get_file_path(filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Error: {filename} file not found at {filepath}")
        
        try:
            return pd.read_excel(filepath, skiprows=skiprows)
        except Exception as e:
            raise Exception(f"Error reading {filename}: {e}")
    
    @staticmethod
    def prepare_statement(bank_statement):
        """
        Prepare bank statement for processing.
        
        Args:
            bank_statement: DataFrame from XLS file
            
        Returns:
            Prepared DataFrame with date column and month grouping
        """
        # Convert first column to datetime with dd/mm/yy format
        date_column = pd.to_datetime(bank_statement.iloc[:, 0], format='%d/%m/%y', errors='coerce')
        
        # Create a new dataframe with only valid date rows
        bank_statement['_date'] = date_column
        bank_statement = bank_statement.dropna(subset=['_date'])
        
        # Group by month
        bank_statement['month'] = bank_statement['_date'].dt.to_period('M')
        
        return bank_statement
