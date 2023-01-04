from helpful_scripts import getAcount
from brownie import FundMe


def fund():
    account = getAcount()
    fund_me = FundMe[-1]
    entrence_fee = fund_me.getEntranceFee()
    # print(entrence_fee)
    print(f"the current entrance fee is: {entrence_fee}")
    print("funding...")
    fund_me.fund({"from": account, "value": entrence_fee + 1})
    print(fund_me.addressToAmountFunded(account.address))


def withdrawl():
    account = getAcount()
    fund_me = FundMe[-1]
    print("withdrawing...")
    fund_me.withdraw(({"from": account}))
    print(fund_me.addressToAmountFunded(account.address))


def main():
    fund()
    withdrawl()
