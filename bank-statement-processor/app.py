"""Flask web application for bank statement processor."""

from flask import Flask, render_template, request, jsonify
import os
import tempfile
from werkzeug.utils import secure_filename
from database import DatabaseManager
from file_manager import FileManager
from statement_processor import StatementProcessor
from html_report_generator import HTMLReportGenerator

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

# Initialize database on startup
try:
    db_manager = DatabaseManager()
    categories = db_manager.fetch_categories()
    alias_to_category = db_manager.build_alias_map(categories)
except Exception as e:
    print(f"Warning: Could not connect to MongoDB: {e}")
    db_manager = None
    categories = []
    alias_to_category = {}


@app.route('/')
def index():
    """Render the upload page."""
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload and generate report."""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.endswith(('.xls', '.xlsx')):
            return jsonify({'error': 'Only XLS/XLSX files are supported'}), 400
        
        # Check if database is connected
        if not db_manager or not categories:
            return jsonify({'error': 'Database not connected. Please ensure MongoDB is running'}), 500
        
        # Save uploaded file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Read and prepare bank statement
            bank_statement = FileManager.read_bank_statement_from_path(filepath, skiprows=22)
            bank_statement = FileManager.prepare_statement(bank_statement)
            
            # Process statement by month
            processor = StatementProcessor(categories, alias_to_category)
            monthly_spending, unprocessed_rows, row_stats = processor.process_monthly_statements(bank_statement)
            
            # Generate HTML report
            html_report = HTMLReportGenerator.generate_report_html(
                bank_statement, monthly_spending, unprocessed_rows, row_stats
            )
            
            return jsonify({'report': html_report}), 200
        
        finally:
            # Clean up temporary file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
