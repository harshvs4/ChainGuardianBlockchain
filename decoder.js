import Web3 from 'web3';

const isValidAddress = Web3.utils.isAddress('');
console.log(isValidAddress);