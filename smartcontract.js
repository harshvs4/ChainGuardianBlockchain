[
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
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
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
	}
]

