import streamlit as st
import os
import pandas as pd
from extraction import extract_tables, parse_financial_data
from calculations import calculate_ratios
from decision_engine import evaluate_loan_eligibility

st.set_page_config(page_title="Loan Eligibility App", layout="centered")
st.title(" Loan Eligibility Assessment Tool")

st.write("Please upload all 3 financial statements (in PDF format):")

pnl_file = st.file_uploader("Profit & Loss Statement", type=["pdf"])
balance_file = st.file_uploader("Balance Sheet", type=["pdf"])
cashflow_file = st.file_uploader("Cash Flow Statement", type=["pdf"])

if pnl_file and balance_file and cashflow_file:

    # Save files temporarily
    with open("pnl.pdf", "wb") as f:
        f.write(pnl_file.getbuffer())

    with open("balance.pdf", "wb") as f:
        f.write(balance_file.getbuffer())

    with open("cashflow.pdf", "wb") as f:
        f.write(cashflow_file.getbuffer())

    st.success("✅ All files uploaded successfully!")

    # Extract data
    pnl_tables = extract_tables("pnl.pdf")
    balance_tables = extract_tables("balance.pdf")
    cashflow_tables = extract_tables("cashflow.pdf")

    pnl_data = parse_financial_data(pnl_tables)
    balance_data = parse_financial_data(balance_tables)
    cashflow_data = parse_financial_data(cashflow_tables)

    # Combine extracted data
    combined_data = {
        'Revenue': pnl_data.get('Revenue'),
        'Net Income': pnl_data.get('Net Income'),
        'Total Assets': balance_data.get('Total Assets'),
        'Total Liabilities': balance_data.get('Total Liabilities'),
        'Current Assets': balance_data.get('Current Assets'),
        'Current Liabilities': balance_data.get('Current Liabilities'),
        'Operating Cash Flow': cashflow_data.get('Operating Cash Flow')
    }

    st.subheader("📄 Extracted Financial Data")
    st.write(pd.DataFrame(combined_data.items(), columns=["Item", "Value"]))

    # Calculate ratios
    ratios = calculate_ratios(combined_data)

    # Display ratios cleanly
    st.subheader("📈 Financial Ratios")
    ratio_df = pd.DataFrame(
        [(key, f"{value:.2f}" if value is not None else "N/A")
         for key, value in ratios.items()],
        columns=["Ratio", "Value"]
    )
    st.table(ratio_df)

    # Loan decision
    decision, reasons = evaluate_loan_eligibility(ratios)

    st.subheader("💳 Loan Eligibility Decision")
    st.write(f"**Decision:** {decision}")

    st.write("**Reasons:**")
    for reason in reasons:
        st.write(f"- {reason}")

    # Clean up temp files
    os.remove("pnl.pdf")
    os.remove("balance.pdf")
    os.remove("cashflow.pdf")
