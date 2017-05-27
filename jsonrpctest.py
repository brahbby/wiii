from web3 import Web3, KeepAliveRPCProvider, IPCProvider

# Note that you should create only one RPCProvider per
# process, as it recycles underlying TCP/IP network connections between
# your process and Ethereum node
web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))

# or for an IPC based connection
#web3 = Web3(IPCProvider())

print web3.eth.blockNumber
print web3.eth.accounts
print web3.eth.getBalance("0x123abc")
print web3.eth.syncing
