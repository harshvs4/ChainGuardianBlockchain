import pandas as pd

###############################################################################
# Scoring Dictionaries & Functions
###############################################################################

# 1. Purpose Risk Scores
#    Include the new high-risk purposes.
purpose_score_dict = {
    "savings": 1,
    "remittance": 2,
    "trade": 3,
    "investment": 3,
    "unusual_investment": 5,
    "unregistered_trade": 5,
    "high_value_transfer": 5,
    "offshore_account": 5,
    "untracked_funds": 5
}

# 2. Currency Risk Scores
#    Adjust to match your institution's risk appetite.
currency_score_dict = {
    "USDT": 2,
    "ETH": 2,
    "BTC": 3,
    # If the CSV might contain other tokens,
    # you can default them to 2 or adjust as needed
}

# 3. High-Risk Countries (Example)
#    In real usage, update this list based on FATF, OFAC, or local regulations.
high_risk_countries = {"China", "Iran", "North Korea", "Syria", "Russia"}

def aml_kyc_score(is_verified: bool) -> int:
    """
    If AML/KYC is True, score low risk (1). 
    If False, score high risk (5).
    """
    return 1 if is_verified else 5

def amount_score(amount: float) -> int:
    """
    Score transaction amounts on a 1–5 scale. 
    Convert crypto to USD or your base fiat if needed.
    """
    if amount < 3000:
        return 1
    elif amount < 10000:
        return 2
    elif amount < 50000:
        return 3
    elif amount < 100000:
        return 4
    else:
        return 5

def geolocation_score(sender_country: str, receiver_country: str) -> int:
    """
    If either the sender or receiver is in a high-risk country, 
    assign a high score (5). Otherwise, 1.
    """
    if sender_country in high_risk_countries or receiver_country in high_risk_countries:
        return 5
    else:
        return 1

def currency_score(currency: str) -> int:
    """
    Lookup in the currency_score_dict; 
    default to 2 if not explicitly listed.
    """
    return currency_score_dict.get(currency, 2)

def purpose_score(purpose: str) -> int:
    """
    Lookup in the purpose_score_dict; default to 3 if not found.
    """
    return purpose_score_dict.get(purpose, 3)

def calculate_risk_score(row) -> int:
    """
    Calculate the total additive risk score for one transaction row.
    """
    kyc = aml_kyc_score(row["AML_KYC_Verified"])
    amt = amount_score(row["Amount"])
    geo = geolocation_score(row["Geolocation_Sender"], row["Geolocation_Receiver"])
    purp = purpose_score(row["Purpose"])
    curr = currency_score(row["Currency"])
    
    return kyc + amt + geo + purp + curr

def categorize_risk(score: int) -> str:
    """
    Categorize risk score into Low, Medium, High, or Very High based on thresholds.
    """
    if score <= 10:
        return "Low"
    elif score <= 15:
        return "Medium"
    elif score <= 20:
        return "High"
    else:
        return "Very High"

def add_risk_score_to_csv(input_csv: str, output_csv: str) -> None:
    # Read CSV data into a DataFrame
    df = pd.read_csv(input_csv)
    
    # Create a new column 'Risk_Score' by applying the risk function
    df["Risk_Score"] = df.apply(calculate_risk_score, axis=1)

    # Add Risk Category
    df["Risk_Category"] = df["Risk_Score"].apply(categorize_risk)
    
    # Export the updated DataFrame to a new CSV
    df.to_csv(output_csv, index=False)
    print(f"Risk scores added to '{input_csv}' and saved as '{output_csv}'.")


if __name__ == "__main__":
    input_file = "merged_file.csv"
    output_file = "transactions_with_risk.csv"
    
    add_risk_score_to_csv(input_file, output_file)