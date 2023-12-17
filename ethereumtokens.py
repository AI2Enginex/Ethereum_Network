

class DAI:

    def __init__(self):

        self.address = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
        self.dai_abi = [
            {
                "constant": True,
                "inputs": [],
                "name": "name",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_spender",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint256"
                    }
                ],
                "name": "approve",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "totalSupply",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_from",
                        "type": "address"
                    },
                    {
                        "name": "_to",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint256"
                    }
                ],
                "name": "transferFrom",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint8"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [
                    {
                        "name": "_owner",
                        "type": "address"
                    }
                ],
                "name": "balanceOf",
                "outputs": [
                    {
                        "name": "balance",
                        "type": "uint256"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "symbol",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_to",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint256"
                    }
                ],
                "name": "transfer",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_spender",
                        "type": "address"
                    },
                    {
                        "name": "_subtractedValue",
                        "type": "uint256"
                    }
                ],
                "name": "decreaseApproval",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "_spender",
                        "type": "address"
                    }
                ],
                "name": "allowance",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_spender",
                        "type": "address"
                    },
                    {
                        "name": "_addedValue",
                        "type": "uint256"
                    }
                ],
                "name": "increaseApproval",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "name": "owner",
                        "type": "address"
                    },
                    {
                        "name": "spender",
                        "type": "address"
                    },
                    {
                        "name": "value",
                        "type": "uint256"
                    }
                ],
                "name": "Approval",
                "type": "event"
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "name": "from",
                        "type": "address"
                    },
                    {
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "name": "value",
                        "type": "uint256"
                    }
                ],
                "name": "Transfer",
                "type": "event"
            }
        ]


class Link:

    def __init__(self):

        self.address = "0x514910771AF9Ca656af840dff83E8264EcF986CA"
        self.link_abi = [{"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}, {"name": "_data", "type": "bytes"}], "name": "transferAndCall", "outputs": [{"name": "success", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_subtractedValue", "type": "uint256"}], "name": "decreaseApproval", "outputs": [{"name": "success", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"name": "_owner", "type": "address"}],
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [{"name": "success", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_addedValue", "type": "uint256"}], "name": "increaseApproval", "outputs": [{"name": "success", "type": "bool"}], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable": False, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": True, "name": "from", "type": "address"}, {"indexed": True, "name": "to", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}, {"indexed": False, "name": "data", "type": "bytes"}], "name": "Transfer", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "name": "owner", "type": "address"}, {"indexed": True, "name": "spender", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}]


class Tether:

    def __init__(self):
        self.address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        self.tether_abi = [{"constant": True, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_upgradedAddress", "type": "address"}], "name": "deprecate", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "deprecated", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_evilUser", "type": "address"}], "name": "addBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "upgradedAddress", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "balances", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "maximumFee", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "_totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [], "name": "unpause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"name": "_maker", "type": "address"}], "name": "getBlackListStatus", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}], "name": "allowed", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "paused", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [{"name": "who", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [], "name": "pause", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "getOwner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [
        ], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "newBasisPoints", "type": "uint256"}, {"name": "newMaxFee", "type": "uint256"}], "name": "setParams", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "issue", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "amount", "type": "uint256"}], "name": "redeem", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [], "name": "basisPointsRate", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": True, "inputs": [{"name": "", "type": "address"}], "name": "isBlackListed", "outputs": [{"name": "", "type": "bool"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "_clearedUser", "type": "address"}], "name": "removeBlackList", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "MAX_UINT", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}, {"constant": False, "inputs": [{"name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": False, "inputs": [{"name": "_blackListedUser", "type": "address"}], "name": "destroyBlackFunds", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"name": "_initialSupply", "type": "uint256"}, {"name": "_name", "type": "string"}, {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint256"}], "payable": False, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Issue", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "amount", "type": "uint256"}], "name": "Redeem", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "newAddress", "type": "address"}], "name": "Deprecate", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "feeBasisPoints", "type": "uint256"}, {"indexed": False, "name": "maxFee", "type": "uint256"}], "name": "Params", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "_blackListedUser", "type": "address"}, {"indexed": False, "name": "_balance", "type": "uint256"}], "name": "DestroyedBlackFunds", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "AddedBlackList", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": False, "name": "_user", "type": "address"}], "name": "RemovedBlackList", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "name": "owner", "type": "address"}, {"indexed": True, "name": "spender", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": False, "inputs": [{"indexed": True, "name": "from", "type": "address"}, {"indexed": True, "name": "to", "type": "address"}, {"indexed": False, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"anonymous": False, "inputs": [], "name": "Pause", "type": "event"}, {"anonymous": False, "inputs": [], "name": "Unpause", "type": "event"}]


class USD_coin:

    def __init__(self):

        self.address = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        self.usdc_abi = [
            {
                "constant": True,
                "inputs": [
                    {
                        "name": "_owner",
                        "type": "address"
                    }
                ],
                "name": "balanceOf",
                "outputs": [
                    {
                        "name": "balance",
                        "type": "uint256"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [],
                "name": "decimals",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint8"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_to",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint256"
                    }
                ],
                "name": "transfer",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": False,
                "inputs": [
                    {
                        "name": "_spender",
                        "type": "address"
                    },
                    {
                        "name": "_value",
                        "type": "uint256"
                    }
                ],
                "name": "approve",
                "outputs": [
                    {
                        "name": "",
                        "type": "bool"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "function"
            },
            {
                "constant": True,
                "inputs": [
                    {
                        "name": "_owner",
                        "type": "address"
                    },
                    {
                        "name": "_spender",
                        "type": "address"
                    }
                ],
                "name": "allowance",
                "outputs": [
                    {
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "payable": False,
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "name": "_initialSupply",
                        "type": "uint256"
                    },
                    {
                        "name": "_name",
                        "type": "string"
                    },
                    {
                        "name": "_symbol",
                        "type": "string"
                    },
                    {
                        "name": "_decimals",
                        "type": "uint8"
                    },
                    {
                        "name": "_minter",
                        "type": "address"
                    }
                ],
                "payable": False,
                "stateMutability": "nonpayable",
                "type": "constructor"
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "name": "owner",
                        "type": "address"
                    },
                    {
                        "indexed": True,
                        "name": "spender",
                        "type": "address"
                    },
                    {
                        "indexed": False,
                        "name": "value",
                        "type": "uint256"
                    }
                ],
                "name": "Approval",
                "type": "event"
            },
            {
                "anonymous": False,
                "inputs": [
                    {
                        "indexed": True,
                        "name": "from",
                        "type": "address"
                    },
                    {
                        "indexed": True,
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "indexed": False,
                        "name": "value",
                        "type": "uint256"
                    }
                ],
                "name": "Transfer",
                "type": "event"
            }
        ]
