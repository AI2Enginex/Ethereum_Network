from web3 import Web3
from ethereumtokens import DAI, Tether, Link, USD_coin


class GetTokens:

    def __init__(self):

        self.tether = Tether()
        self.usdc = USD_coin()


class MaketConnection:

    def __init__(self, url, address):

        self.web3 = Web3(Web3.HTTPProvider(url))
        self.eth_address = address


class ReadBalance(MaketConnection):

    def __init__(self, url, address):

        super().__init__(url, address)
        

    def get_token_balance(self, token_address, token_abi):

        try:
            token_contract = self.web3.eth.contract(
                address=token_address, abi=token_abi)
            token_balance = token_contract.functions.balanceOf(
                self.eth_address).call()
            return token_balance
        except Exception as e:
            return f'error: {e}'
    

    def mainet_token(self):

        try:
            return self.web3.from_wei(self.web3.eth.get_balance(self.eth_address), 'ether')
        except Exception as e:
            return e
    def get_token_exact_value(self, token_address, token_abi):

        try:
            return self.web3.from_wei(self.get_token_balance(token_address, token_abi), 'ether')
        except Exception as e:
            return f"error: {e}"


class ReadTokenBalance(GetTokens):

    def __init__(self, url, address):

        super().__init__()
        self.read_balance = ReadBalance(url=url, address=address)
    

    def get_ethereum_balance(self):

        try:
            return f"{self.read_balance.mainet_token()} ETH"
        except Exception as e:
            return f"error: {e}"
        
    def get_tether_balance(self):

        try:
            return f"{self.read_balance.get_token_exact_value(self.tether.address,self.tether.tether_abi)} TETHER"
        except Exception as e:
            return f"error: {e}"

    def get_usdc_balance(self):

        try:
            return f"{self.read_balance.get_token_exact_value(self.usdc.address,self.usdc.usdc_abi)}  USDC"
        except Exception as e:
            return e


if __name__ == '__main__':

    balance = ReadTokenBalance(url='https://mainnet.infura.io/v3/6df36ff34190461dbd182dbd4b0c56ef',
                               address='0xF977814e90dA44bFA03b6295A0616a897441aceC')
    
    print('Ethereum: ',balance.get_ethereum_balance())
    print('tether: ',balance.get_tether_balance())
    print('USDC: ',balance.get_usdc_balance())