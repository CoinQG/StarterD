from brownie import accounts, FundMe, MockV3Aggregator, config, network
from helpful_scripts import getAcount, deploy_moks, Local_BlockChain_Envirenemet


def Deploy_FundMe():
    account = getAcount()

    if network.show_active() not in Local_BlockChain_Envirenemet:
        perice_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"the active network is:{network.show_active()}")
        print("depllying moks....")
        deploy_moks()
        perice_feed_address = MockV3Aggregator[-1].address

    Fund_Me = FundMe.deploy(
        perice_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    print(f"contract deployed at: {Fund_Me.address}")


def main():
    Deploy_FundMe()
