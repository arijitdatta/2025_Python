"""Database operations for bank statement processor."""

from pymongo import MongoClient


class DatabaseManager:
    """Manages MongoDB connections and category fetching."""
    
    def __init__(self, connection_string='mongodb://localhost:27017/', db_name='statementprocessordb'):
        """
        Initialize database connection.
        
        Args:
            connection_string: MongoDB connection string
            db_name: Database name
        """
        try:
            self.client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB")
            self.db = self.client[db_name]
            self.categories_collection = self.db['categories']
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise
    
    def fetch_categories(self):
        """Fetch all categories from MongoDB."""
        return list(self.categories_collection.find())
    
    def print_categories(self, categories):
        """Print categories to console."""
        print("Categories from MongoDB:")
        for category in categories:
            print(f"  Name: {category['name']}, Aliases: {category['aliases']}")
        print()
    
    def build_alias_map(self, categories):
        """
        Build a mapping of aliases to category names.
        
        Args:
            categories: List of category dictionaries
            
        Returns:
            Dictionary mapping aliases to category names
        """
        alias_to_category = {}
        for category in categories:
            name = category['name']
            aliases = category['aliases'].split(',')
            for alias in aliases:
                alias_to_category[alias.strip().lower()] = name
        return alias_to_category
