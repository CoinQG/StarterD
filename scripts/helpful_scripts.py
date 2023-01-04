from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000
Local_BlockChain_Envirenemet = ["development", "ganache-local"]


def getAcount():
    if network.show_active() in Local_BlockChain_Envirenemet:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_moks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": getAcount().address}
        )
    print("moks deployed!")
