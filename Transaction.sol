
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract TransactionStore {
    // Core transaction details
    struct CoreTransaction {
        address sender;
        address receiver;
        uint256 amount;
        string currency_type;
        uint256 timestamp;
        uint256 gas_fee;
    }

    // Compliance and metadata
    struct ComplianceDetails {
        string transaction_type;
        string geolocation_sender;
        string geolocation_receiver;
        bool watchlist_match;
        bool aml_kyc_verified;
        string purpose_of_transaction;
        bool cross_border_transaction;
        string regulatory_region;
    }

    // Separate storage for different components
    mapping(string => CoreTransaction) public coreTransactions;
    mapping(string => ComplianceDetails) public complianceData;

    // Events
    event TransactionAdded(string transaction_id);

    // Store a new transaction
    function storeTransaction(
        address receiver,
        uint256 amount,
        string memory currency_type,
        uint256 gas_fee,
        string memory transaction_type,
        string memory geolocation_sender,
        string memory geolocation_receiver,
        bool watchlist_match,
        bool aml_kyc_verified,
        string memory purpose_of_transaction,
        bool cross_border_transaction,
        string memory regulatory_region
    ) public {
        // Generate a unique transaction ID
        string memory transaction_id = _generateTransactionId(msg.sender, block.timestamp);

        // Store core transaction details
        coreTransactions[transaction_id] = CoreTransaction(
            msg.sender,
            receiver,
            amount,
            currency_type,
            block.timestamp,
            gas_fee
        );

        // Store compliance details
        complianceData[transaction_id] = ComplianceDetails(
            transaction_type,
            geolocation_sender,
            geolocation_receiver,
            watchlist_match,
            aml_kyc_verified,
            purpose_of_transaction,
            cross_border_transaction,
            regulatory_region
        );

        emit TransactionAdded(transaction_id);
    }

    // Retrieve all details for a transaction
    function getTransactionDetails(string memory transaction_id)
        public
        view
        returns (
            CoreTransaction memory core,
            ComplianceDetails memory compliance
        )
    {
        return (coreTransactions[transaction_id], complianceData[transaction_id]);
    }

    // Internal function to generate a unique transaction ID
    function _generateTransactionId(address sender, uint256 timestamp) internal pure returns (string memory) {
        return _toHex(keccak256(abi.encode(sender, timestamp)));
    }

    // Helper function to convert bytes32 hash to a hexadecimal string
    function _toHex(bytes32 data) internal pure returns (string memory) {
        bytes memory alphabet = "0123456789abcdef";
        bytes memory str = new bytes(2 + data.length * 2);
        str[0] = "0";
        str[1] = "x";
        for (uint256 i = 0; i < data.length; i++) {
            str[2 + i * 2] = alphabet[uint8(data[i] >> 4)];
            str[3 + i * 2] = alphabet[uint8(data[i] & 0x0f)];
        }
        return string(str);
    }
}