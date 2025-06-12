def calculate_ratios(data):
    ratios = {}

    try:
        ratios['Profit Margin'] = data['Net Income'] / data['Revenue'] if data['Revenue'] else None
    except:
        ratios['Profit Margin'] = None

    try:
        ratios['Debt to Assets'] = data['Total Liabilities'] / data['Total Assets'] if data['Total Assets'] else None
    except:
        ratios['Debt to Assets'] = None

    try:
        ratios['Current Ratio'] = data['Current Assets'] / data['Current Liabilities'] if data['Current Liabilities'] else None
    except:
        ratios['Current Ratio'] = None

    try:
        ratios['Operating Cash Flow Ratio'] = data['Operating Cash Flow'] / data['Current Liabilities'] if data['Current Liabilities'] else None
    except:
        ratios['Operating Cash Flow Ratio'] = None

    return ratios
