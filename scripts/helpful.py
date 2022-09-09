from brownie import accounts, network, config


def get_account():
    if network.show_active == "development":
        return accounts[2]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print(get_account())
