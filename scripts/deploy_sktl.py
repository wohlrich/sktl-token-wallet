from brownie import SKTL, network, config
from scripts.helpful_scripts import get_account, get_contract
import shutil
import os
import yaml
import json
from web3 import Web3
import pandas as pd
import logbook
import sys

logger = logbook.Logger('deploy_sktl')
logbook.StreamHandler(sys.stdout).push_application()

# KEPT_BALANCE = Web3.toWei(100, "ether")


def deploy_sktls(update_front_end=False):
    account = get_account()
    sktl_token = SKTL.deploy({"from": account}, publish_source=True)
    if update_front_end:
        # copy_front_end()
        pass

    logger.info(f'{sktl_token=}')
    logger.info(f'{sktl_token.totalSupply()=}')


def get_total_supply():
    account = get_account()
    logger.info(f"total supply = {SKTL[0].totalSupply({'from': account}) / 10 ** 18}")
    logger.info(f"owner account = {SKTL[0].balanceOf(account) / 10 ** 18}")

# def add_reward():
#     account = get_account()
#     sktl = Sktl20.at('0x292135fF911E6081ecC90F3bD1f9CDaAED5C78cD')
#     sktl.rewards(5300 * (10 ** 18), {"from": account})
# 
# def copy_front_end():
#     print("Updating front end...")
#     # The Build
#     copy_folders_to_front_end("./build/contracts", "./front_end/src/chain-info")
# 
#     # The Contracts
#     copy_folders_to_front_end("./contracts", "./front_end/src/contracts")
# 
#     # The ERC20
#     copy_files_to_front_end(
#         "./build/contracts/dependencies/OpenZeppelin/openzeppelin-contracts@4.3.2/ERC20.json",
#         "./front_end/src/chain-info/ERC20.json",
#     )
#     # The Map
#     copy_files_to_front_end(
#         "./build/deployments/map.json", "./front_end/src/chain-info/map.json",
#     )
# 
#     # The Config, converted from YAML to JSON
#     with open("brownie-config.yaml", "r") as brownie_config:
#         config_dict = yaml.load(brownie_config, Loader=yaml.FullLoader)
#         with open(
#             "./front_end/src/brownie-config-json.json", "w"
#         ) as brownie_config_json:
#             json.dump(config_dict, brownie_config_json)
#     print("Front end updated!")
# 
# 
# def copy_folders_to_front_end(src, dest):
#     if os.path.exists(dest):
#         shutil.rmtree(dest)
#     shutil.copytree(src, dest)
# 
# 
# def copy_files_to_front_end(src, dest):
#     if os.path.exists(dest):
#         os.remove(dest)
#     shutil.copyfile(src, dest)
# 
# 
# def air_drop():
#     df = pd.read_csv('/Users/danielng/projects/sktls-defi/temp/sktl_init_drop_address.csv')
#     for addr in df.address:
#         Sktl20[-1].transfer(addr, 1000 * (10 ** 18), {"from": get_account(0)})
# 

def main():
    deploy_sktls(update_front_end=False)
