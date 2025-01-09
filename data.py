from web3 import Web3
import random
import time

# Blockchain connection
provider = ""
web3 = Web3(Web3.HTTPProvider(provider))

if not web3.is_connected():
    raise Exception("Web3 is not connected. Check your provider URL.")

# Contract details
contract_address = ""
contract_address = Web3.to_checksum_address(contract_address)

contract_abi = [  
    
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "currency_type",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "gas_fee",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "transaction_type",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "geolocation_sender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "geolocation_receiver",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "watchlist_match",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "aml_kyc_verified",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "purpose_of_transaction",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "cross_border_transaction",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "regulatory_region",
				"type": "string"
			}
		],
		"name": "storeTransaction",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": False,
				"internalType": "string",
				"name": "transaction_id",
				"type": "string"
			}
		],
		"name": "TransactionAdded",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "complianceData",
		"outputs": [
			{
				"internalType": "string",
				"name": "transaction_type",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "geolocation_sender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "geolocation_receiver",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "watchlist_match",
				"type": "bool"
			},
			{
				"internalType": "bool",
				"name": "aml_kyc_verified",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "purpose_of_transaction",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "cross_border_transaction",
				"type": "bool"
			},
			{
				"internalType": "string",
				"name": "regulatory_region",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "coreTransactions",
		"outputs": [
			{
				"internalType": "address",
				"name": "sender",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "receiver",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "amount",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "currency_type",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "timestamp",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "gas_fee",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getAllTransactionIds",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "transaction_id",
				"type": "string"
			}
		],
		"name": "getTransactionDetails",
		"outputs": [
			{
				"components": [
					{
						"internalType": "address",
						"name": "sender",
						"type": "address"
					},
					{
						"internalType": "address",
						"name": "receiver",
						"type": "address"
					},
					{
						"internalType": "uint256",
						"name": "amount",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "currency_type",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "timestamp",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "gas_fee",
						"type": "uint256"
					}
				],
				"internalType": "struct TransactionStore.CoreTransaction",
				"name": "core",
				"type": "tuple"
			},
			{
				"components": [
					{
						"internalType": "string",
						"name": "transaction_type",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "geolocation_sender",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "geolocation_receiver",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "watchlist_match",
						"type": "bool"
					},
					{
						"internalType": "bool",
						"name": "aml_kyc_verified",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "purpose_of_transaction",
						"type": "string"
					},
					{
						"internalType": "bool",
						"name": "cross_border_transaction",
						"type": "bool"
					},
					{
						"internalType": "string",
						"name": "regulatory_region",
						"type": "string"
					}
				],
				"internalType": "struct TransactionStore.ComplianceDetails",
				"name": "compliance",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "transactionIds",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}

]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Wallet details
sender_address = ""
private_key = ""

# Generate random transaction data
def generate_transaction():
    geolocations = ["United States", "China", "Germany", "India", "Singapore", "Japan"]
    purposes = ["investment", "trade", "remittance", "savings"]
    currencies = ["USDT", "BTC", "ETH"]

    random_receiver = f"0x{''.join(random.choices('abcdef0123456789', k=40))}"
    checksum_receiver = Web3.to_checksum_address(random_receiver)  # Convert to checksum format

    return {
        "receiver": checksum_receiver,
        "amount": round(random.uniform(0.1, 10000), 2),
        "currency_type": random.choice(currencies),
        "gas_fee": round(random.uniform(0.0001, 0.01), 4),
        "transaction_type": random.choice(["peer_to_peer", "exchange", "smart_contract"]),
        "geolocation_sender": random.choice(geolocations),
        "geolocation_receiver": random.choice(geolocations),
        "watchlist_match": random.choice([True, False]),
        "aml_kyc_verified": random.choice([True, False]),
        "purpose_of_transaction": random.choice(purposes),
        "cross_border_transaction": random.choice([True, False]),
        "regulatory_region": random.choice(["US", "EU", "APAC"]),
    }

# Send transaction data to the blockchain
def send_transaction(transaction):
    try:
        base_gas_price = web3.eth.gas_price
        current_nonce = web3.eth.get_transaction_count(sender_address, "pending")  # Include pending transactions

        tx = contract.functions.storeTransaction(
            transaction["receiver"],
            int(transaction["amount"] * 1e18),  # Convert to smallest unit (e.g., wei)
            transaction["currency_type"],
            int(transaction["gas_fee"] * 1e18),  # Convert to smallest unit (e.g., wei)
            transaction["transaction_type"],
            transaction["geolocation_sender"],
            transaction["geolocation_receiver"],
            transaction["watchlist_match"],
            transaction["aml_kyc_verified"],
            transaction["purpose_of_transaction"],
            transaction["cross_border_transaction"],
            transaction["regulatory_region"],
        ).build_transaction(
            {
                "from": sender_address,
                "gas": 3000000,
                "gasPrice": int(base_gas_price * 1.2),  # Increase gas price by 20%
                "nonce": current_nonce,  # Use the correct nonce
            }
        )

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"Transaction sent with hash: {web3.to_hex(tx_hash)}")
        return tx_hash

    except Exception as e:
        print(f"Error sending transaction: {e}")
        return None

# Simulate transactions with anomalies
def simulate_transactions(count):
    print(f"Simulating {count} transactions...")
    for i in range(count):
        transaction = generate_transaction()

        # Introduce anomalies (e.g., very high amounts or missing KYC)
        if random.random() < 0.1:  # 10% chance of anomaly
            transaction["amount"] = round(random.uniform(100000, 1000000), 2)
            transaction["aml_kyc_verified"] = False

        tx_hash = send_transaction(transaction)
        if tx_hash:
            print(f"Transaction confirmed: {web3.to_hex(tx_hash)}")
        time.sleep(2)  # Slight delay to avoid nonce overlap


# Fetch transaction IDs
def fetch_transaction_ids():
    try:
        transaction_ids = contract.functions.getAllTransactionIds().call()
        print("Transaction IDs:", transaction_ids)
        return transaction_ids
    except Exception as e:
        print(f"Error fetching transaction IDs: {e}")
        return []

if __name__ == "__main__":
    balance = web3.eth.get_balance(sender_address)
    print(f"Balance of sender: {web3.from_wei(balance, 'ether')} ETH")

    # Fetch all transaction IDs
    transaction_ids = fetch_transaction_ids()

    # Simulate sending new transactions
    simulate_transactions(10)