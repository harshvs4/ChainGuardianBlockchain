import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate a random TransactionID
def generate_transaction_id():
    return f"0x{''.join(random.choices('abcdef0123456789', k=64))}"

# Function to generate a single transaction
def generate_transaction(repeated_senders=None):
    geolocations = ["United States", "Dubai", "Germany", "India", "Singapore", "Japan"]
    purposes = ["investment", "trade", "remittance", "savings"]
    currencies = ["USDT", "BTC", "ETH"]

    # Reuse a sender address for some transactions to simulate history
    sender = random.choice(repeated_senders) if repeated_senders and random.random() < 0.3 else f"0x{''.join(random.choices('abcdef0123456789', k=40))}"

    return {
        "TransactionID": generate_transaction_id(),
        "Sender": sender,
        "Receiver": f"0x{''.join(random.choices('abcdef0123456789', k=40))}",
        "Amount": round(random.uniform(0.1, 10000), 2),
        "Currency": random.choice(currencies),
        "GasFee": round(random.uniform(0.0001, 0.01), 4),
        "Timestamp": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d %H:%M:%S"),
        "Purpose": random.choice(purposes),
        "Region": random.choice(["US", "EU", "APAC"]),
        "AML_KYC_Verified": random.choice([True, False]),
        "Geolocation_Receiver": random.choice(geolocations),
        "Geolocation_Sender": random.choice(geolocations),
    }

# Function to simulate transactions with anomalies
def simulate_transactions(count, anomaly_percentage=0.03):
    print(f"Simulating {count} transactions with {int(count * anomaly_percentage)} anomalies...")

    # Generate some repeatable sender addresses
    repeated_senders = [f"0x{''.join(random.choices('abcdef0123456789', k=40))}" for _ in range(10)]

    # Generate transactions
    transactions = []
    for _ in range(count):
        transaction = generate_transaction(repeated_senders)
        transactions.append(transaction)

    # Introduce anomalies
    num_anomalies = int(count * anomaly_percentage)
    high_risk_countries = ["China", "Iran", "North Korea", "Syria", "Russia"]
    anomaly_purposes = [
        "unusual_investment",
        "unregistered_trade",
        "high_value_transfer",
        "offshore_account",
        "untracked_funds",
    ]
    for _ in range(num_anomalies):
        anomaly = random.choice(transactions)
        anomaly["Amount"] = round(random.uniform(100000, 1000000), 2)  # Large amounts
        anomaly["AML_KYC_Verified"] = False  # Unverified KYC
        anomaly["Purpose"] = random.choice(anomaly_purposes)  # Subtle suspicious purposes
        anomaly["Geolocation_Sender"] = random.choice(high_risk_countries)  # High-risk countries

    return transactions

# Generate 2000 transactions with 3% anomalies
num_transactions = 20000
transactions = simulate_transactions(num_transactions, anomaly_percentage=0.2)

# Save to CSV
file_path = "simulated_transactions.csv"
df = pd.DataFrame(transactions)
df.to_csv(file_path, index=False)

print(f"Simulated transactions saved to {file_path}")