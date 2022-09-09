from brownie import Bitcoin, interface, config
from scripts.helpful import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    ad = config["address"]["others"]
    token = Bitcoin.deploy(initial_supply, {"from": account})

    tx = token.totalSupply({"from": account})
    tx = Web3.toWei(tx, "ether")
    print(tx)
