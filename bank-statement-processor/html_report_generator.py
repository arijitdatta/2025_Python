"""HTML report generation for bank statement processor."""


class HTMLReportGenerator:
    """Generates HTML reports for bank statement analysis."""
    
    @staticmethod
    def generate_report_html(bank_statement, monthly_spending, unprocessed_rows, row_stats=None):
        """
        Generate HTML report.
        
        Args:
            bank_statement: Processed DataFrame
            monthly_spending: Dictionary of monthly spending by category
            unprocessed_rows: List of unprocessed transaction rows
            row_stats: Dictionary containing debit/credit statistics
            
        Returns:
            HTML string of the report
        """
        html = []
        
        # Header
        html.append(HTMLReportGenerator._get_header())
        
        # Statistics
        html.append(HTMLReportGenerator._get_statistics(bank_statement, unprocessed_rows, row_stats))
        
        # Monthly spending summary
        html.append(HTMLReportGenerator._get_monthly_summary(monthly_spending))
        
        # Unprocessed rows
        html.append(HTMLReportGenerator._get_unprocessed_rows(unprocessed_rows))
        
        # Footer
        html.append(HTMLReportGenerator._get_footer())
        
        return '\n'.join(html)
    
    @staticmethod
    def _get_header():
        """Get HTML header."""
        return """
        <div class="header">
            <h1>BANK STATEMENT ANALYSIS REPORT</h1>
        </div>
        """
    
    @staticmethod
    def _get_statistics(bank_statement, unprocessed_rows, row_stats=None):
        """Get HTML statistics section."""
        total_rows = len(bank_statement)
        total_unprocessed = len(unprocessed_rows)
        total_processed = total_rows - total_unprocessed
        
        html = f"""
        <div class="section">
            <h2>Overall Statistics</h2>
            <table class="stats-table">
                <tr>
                    <td><strong>Total Rows:</strong></td>
                    <td>{total_rows}</td>
                </tr>
                <tr>
                    <td><strong>Processed Rows:</strong></td>
                    <td>{total_processed}</td>
                </tr>
        """
        
        # Add debit/credit breakdown if available
        if row_stats:
            total_debit = row_stats.get('total_debit_rows', 0)
            total_credit = row_stats.get('total_credit_rows', 0)
            html += f"""
                <tr>
                    <td style="padding-left: 30px; color: #666;">├─ Debit Rows (spending):</td>
                    <td>{total_debit}</td>
                </tr>
                <tr>
                    <td style="padding-left: 30px; color: #666;">└─ Credit Rows (income):</td>
                    <td>{total_credit}</td>
                </tr>
            """
        
        html += f"""
                <tr>
                    <td><strong>Unprocessed Rows:</strong></td>
                    <td>{total_unprocessed}</td>
                </tr>
            </table>
        </div>
        """
        
        return html
    
    @staticmethod
    def _get_monthly_summary(monthly_spending):
        """Get HTML monthly spending summary."""
        html = ['<div class="section">']
        html.append('<h2>Monthly Spending Summary</h2>')
        
        for month in sorted(monthly_spending.keys()):
            html.append(f'<div class="month-section">')
            html.append(f'<h3>{month}</h3>')
            html.append(f'<div class="sort-buttons">')
            html.append(f'<button class="sort-btn sort-category-btn" data-month="{month}">↕ Sort by Category</button>')
            html.append(f'<button class="sort-btn sort-amount-btn" data-month="{month}">↕ Sort by Amount</button>')
            html.append(f'</div>')
            html.append(f'<table class="spending-table" data-month="{month}">')
            html.append('<thead><tr><th class="sortable" data-sort="category">Category</th><th class="sortable" data-sort="amount">Amount</th></tr></thead>')
            html.append('<tbody>')
            
            for category, amount in monthly_spending[month].items():
                if amount > 0:  # Only show categories with spending
                    html.append(f'<tr data-category="{category}" data-amount="{amount}"><td>{category}</td><td>Rs {amount:.2f}</td></tr>')
            
            html.append('</tbody>')
            html.append('</table>')
            html.append('</div>')
        
        html.append('</div>')
        return '\n'.join(html)
    
    @staticmethod
    def _get_unprocessed_rows(unprocessed_rows):
        """Get HTML unprocessed rows section."""
        html = ['<div class="section">']
        
        if unprocessed_rows:
            html.append('<h2>Unprocessed Rows</h2>')
            html.append('<div class="unprocessed-container">')
            
            current_month = None
            for row_info in unprocessed_rows:
                if row_info['month'] != current_month:
                    if current_month is not None:
                        html.append('</div>')  # Close previous month div
                    current_month = row_info['month']
                    html.append(f'<div class="month-unprocessed">')
                    html.append(f'<h3>{current_month}</h3>')
                
                html.append('<div class="unprocessed-row">')
                html.append(f"<strong>Row {row_info['row_num']}:</strong> {row_info['reason']}")
                
                if 'description' in row_info:
                    if 'debit' in row_info:
                        html.append(f"<br><em>Description: {row_info['description']}, Debit: Rs {row_info['debit']:.2f}</em>")
                    elif 'credit' in row_info:
                        html.append(f"<br><em>Description: {row_info['description']}, Credit: Rs {row_info['credit']:.2f}</em>")
                
                html.append('</div>')
            
            html.append('</div>')  # Close last month div
            html.append('</div>')  # Close unprocessed-container
        else:
            html.append('<div class="success-message">')
            html.append('<h2>✓ Success</h2>')
            html.append('<p>All rows processed successfully!</p>')
            html.append('</div>')
        
        html.append('</div>')
        return '\n'.join(html)
    
    @staticmethod
    def _get_footer():
        """Get HTML footer."""
        return """
        <div class="footer">
            <p>Bank Statement Processor Report</p>
        </div>
        """
