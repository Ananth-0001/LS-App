def evaluate_loan_eligibility(ratios):
    decision = "Reject"
    reasons = []

    if ratios['Profit Margin'] is not None and ratios['Profit Margin'] > 0.1:
        reasons.append("Good Profit Margin")
    else:
        reasons.append("Low Profit Margin")

    if ratios['Debt to Assets'] is not None and ratios['Debt to Assets'] < 0.7:
        reasons.append("Healthy Debt Ratio")
    else:
        reasons.append("High Debt Ratio")

    if ratios['Current Ratio'] is not None and ratios['Current Ratio'] > 1.2:
        reasons.append("Good Liquidity")
    else:
        reasons.append("Low Liquidity")

    if ratios['Operating Cash Flow Ratio'] is not None and ratios['Operating Cash Flow Ratio'] > 0.5:
        reasons.append("Good Cash Flow Coverage")
    else:
        reasons.append("Poor Cash Flow Coverage")

    if reasons.count("Good Profit Margin") >= 1 and reasons.count("Healthy Debt Ratio") >= 1 and reasons.count("Good Liquidity") >= 1:
        decision = "Approve"
    elif reasons.count("Good Profit Margin") + reasons.count("Healthy Debt Ratio") >= 2:
        decision = "Caution"

    return decision, reasons
