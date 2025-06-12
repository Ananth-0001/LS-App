import camelot

def extract_tables(file_path):
    tables = camelot.read_pdf(file_path, pages='1-end', flavor='stream')
    return tables

def parse_financial_data(tables):
    data = {
        'Revenue': None,
        'Net Income': None,
        'Total Assets': None,
        'Total Liabilities': None,
        'Current Assets': None,
        'Current Liabilities': None,
        'Operating Cash Flow': None
    }

    for table in tables:
        df = table.df
        for row in df.values:
            row_text = " ".join(row).lower()

            if "revenue" in row_text and data['Revenue'] is None:
                data['Revenue'] = extract_number(row)

            if ("net income" in row_text or "profit after tax" in row_text) and data['Net Income'] is None:
                data['Net Income'] = extract_number(row)

            if "total assets" in row_text and data['Total Assets'] is None:
                data['Total Assets'] = extract_number(row)

            if "total liabilities" in row_text and data['Total Liabilities'] is None:
                data['Total Liabilities'] = extract_number(row)

            if "current assets" in row_text and data['Current Assets'] is None:
                data['Current Assets'] = extract_number(row)

            if "current liabilities" in row_text and data['Current Liabilities'] is None:
                data['Current Liabilities'] = extract_number(row)

            if "operating cash flow" in row_text and data['Operating Cash Flow'] is None:
                data['Operating Cash Flow'] = extract_number(row)

    return data

def extract_number(row):
    for item in row:
        item = item.replace(",", "").replace("₹", "").replace("$", "").strip()
        try:
            return float(item)
        except:
            continue
    return None
