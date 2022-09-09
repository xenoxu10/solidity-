from brownie import config, network, interface
from scripts.helpful import get_account
from web3 import Web3


def get_Lending_pool():
    account = get_account()
    erc20_address = interface.IERC20(
        config["networks"][network.show_active()]["weth_token"]
    )
    lending_Pool_address_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_Pool_Address_Provider"]
    )
    lending_pool_address = lending_Pool_address_provider.getLendingPool()
    print(lending_pool_address)
    lending_Pool = interface.ILendingPool(lending_pool_address)
    approved_erc = erc20_address.approve({"from": account}, {"value1": 1 * 10**17})
    print("approved!")


def main():
    get_Lending_pool()
