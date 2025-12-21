# Bank Statement Processor - Web UI

A web-based application to process and analyze bank statements.

## Features

- 📤 Upload XLS/XLSX bank statement files
- 🏦 Automatic transaction categorization using MongoDB
- 📊 Monthly spending analysis
- 🔍 Detailed unprocessed transaction tracking
- 🎨 Beautiful, responsive web interface

## Installation

### Prerequisites

- Python 3.7+
- MongoDB running on localhost:27017

### Setup

1. Install required packages:

```bash
pip install -r requirements.txt
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Running the Application

1. Start MongoDB (if not already running):

```bash
# On macOS with Homebrew
brew services start mongodb-community

# Or run Docker container
docker run -d -p 27017:27017 mongo
```

2. Run the Flask application:

```bash
python app.py
```

3. Open your browser and navigate to:

```
http://localhost:5000
```

## Usage

1. **Upload File**: Click or drag-and-drop your bank statement file (XLS/XLSX)
2. **Process**: Click the "Process" button
3. **View Report**: The analysis report will display with:
   - Overall statistics (total, processed, unprocessed rows)
   - Monthly spending summary by category
   - Detailed list of unprocessed transactions

## Supported File Format

Bank statements should have the following structure:

- **Skip first 22 rows** (containing headers/metadata)
- **Column 1**: Date (dd/mm/yy format)
- **Column 2**: Description
- **Column 5**: Debit Amount
- **Column 6**: Credit Amount

## Category Configuration

Categories are fetched from MongoDB collection `categories` with the following structure:

```json
{
  "name": "Groceries",
  "aliases": "grocery, supermarket, walmart, target"
}
```

## File Structure

```
bank-statement-processor/
├── app.py                      # Flask application
├── database.py                 # MongoDB operations
├── file_manager.py             # File handling
├── statement_processor.py       # Transaction processing
├── report_generator.py         # Console report generation
├── html_report_generator.py    # HTML report generation
├── BankStatementReader.py      # CLI entry point
├── requirements.txt            # Python dependencies
├── templates/
│   └── index.html              # Web UI template
└── README.md
```

## API Endpoints

### GET `/`

Returns the main upload page.

### POST `/api/upload`

Uploads and processes a bank statement file.

**Request:**

- Method: POST
- Content-Type: multipart/form-data
- Body: form data with `file` field

**Response:**

```json
{
  "report": "<html report content>"
}
```

**Error Response:**

```json
{
  "error": "Error message"
}
```

## Troubleshooting

### "MongoDB not connected"

- Ensure MongoDB is running on localhost:27017
- Check MongoDB service status

### "File not found"

- Ensure the XLS/XLSX file is valid
- Check file format (must be .xls or .xlsx)

### "No matching category"

- Verify category aliases in MongoDB
- Ensure transaction descriptions contain alias keywords

## Development

To run in development mode with auto-reload:

```bash
python app.py
```

The Flask app will start with debug mode enabled and auto-reload on file changes.
