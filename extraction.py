import camelot
import json
import os

# Load keyword mappings from JSON


def load_keyword_mapping():
    file_path = os.path.join(os.path.dirname(__file__), 'keyword_mapping.json')
    with open(file_path, 'r') as f:
        return json.load(f)


keyword_mapping = load_keyword_mapping()


def extract_tables(file_path):
    tables = camelot.read_pdf(file_path, pages='all', flavor='stream')
    return tables


def parse_financial_data(tables):
    data = {key: None for key in keyword_mapping.keys()}

    for table in tables:
        df = table.df
        for row in df.values:
            row_text = " ".join(row).lower()

            for key, keywords in keyword_mapping.items():
                if data[key] is None:
                    for word in keywords:
                        if word in row_text:
                            data[key] = extract_number(row)
                            break

    return data


def extract_number(row):
    for item in row:
        item = item.replace(",", "").replace("₹", "").replace("$", "").strip()
        try:
            return float(item)
        except:
            continue
    return None
