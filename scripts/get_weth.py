from scripts.helpful import get_account
from brownie import config, network, interface


def main():
    account = get_account()
    weth = interface.IWETH10(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10**18})
