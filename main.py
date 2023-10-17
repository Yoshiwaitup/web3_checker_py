from config import DATA
from web3 import Web3
import time
from termcolor import cprint
import csv
# Available network list
ETH = Web3(Web3.HTTPProvider(DATA.get("ethereum").get("rpc")))
BSC = Web3(Web3.HTTPProvider(DATA.get("bsc").get("rpc")))
POLYGON = Web3(Web3.HTTPProvider(DATA.get("polygon").get("rpc")))
OPTIMISM = Web3(Web3.HTTPProvider(DATA.get("optimism").get("rpc")))
ARB = Web3(Web3.HTTPProvider(DATA.get("arbitrum").get("rpc")))
FTM = Web3(Web3.HTTPProvider(DATA.get("fantom").get("rpc")))
NOVA = Web3(Web3.HTTPProvider(DATA.get("nova").get("rpc")))
ZK = Web3(Web3.HTTPProvider(DATA.get("zksync").get("rpc")))
CELO = Web3(Web3.HTTPProvider(DATA.get("celo").get("rpc")))
LINEA = Web3(Web3.HTTPProvider(DATA.get("linea").get("rpc")))
BASE = Web3(Web3.HTTPProvider(DATA.get("base").get("rpc")))
ZKEVM = Web3(Web3.HTTPProvider(DATA.get("polygon_zkevm").get("rpc")))
AVAX = Web3(Web3.HTTPProvider(DATA.get("avalanche").get("rpc")))
CORE = Web3(Web3.HTTPProvider(DATA.get("core").get("rpc")))
HRM = Web3(Web3.HTTPProvider(DATA.get("harmony").get("rpc")))
GNOSIS = Web3(Web3.HTTPProvider(DATA.get("gnosis").get("rpc")))
MOONBEAM = Web3(Web3.HTTPProvider(DATA.get("moonbeam").get("rpc")))
MOONRIVER = Web3(Web3.HTTPProvider(DATA.get("moonriver").get("rpc")))

rpc_list = [ETH, BSC, POLYGON, OPTIMISM, ARB, FTM, NOVA, ZK, CELO, 
            LINEA, BASE, ZKEVM, AVAX, CORE, HRM, GNOSIS, MOONBEAM, MOONRIVER]
name_list = ["ETH", "BSC", "POLYGON", "OPTIMISM", "ARB", "FTM", "NOVA", "ZK", 
             "CELO","LINEA", "BASE", "ZKEVM", "AVAX", "CORE", "HRM", "GNOSIS", "MOONBEAM", "MOONRIVER"]
def rpc_connection_check(): 
    for i in rpc_list:
        for n in name_list:
            cprint(f"{n} connected: {i.is_connected()}", "green")
        if n == "MOONRIVER":
            break
rpc_connection_check()

refile = open('wallets.txt', 'r') 
reader = csv.reader(refile)
allRows = [row for row in reader]
wallet_list = sum(allRows, [])

cprint("Начинаю проверку балансов доступных сетей", "yellow")

def evm_balance_check():
    answer = input("Желаете ли вы проверить балансы даннных кошельков y/n?, ")
    if answer == 'y':
        for i, network in enumerate(rpc_list):
            namew = name_list[i]
            for w in wallet_list:
                result1 = network.eth.get_balance(w)
                time.sleep(1)
                if result1 > float(0.0):
                    color = "green"
                else:
                    color = "red"
                cprint(f"Баланс кошелька {w} в сети {namew} равняется {Web3.from_wei(result1, 'ether')} ETH", color)
    else:
        print ('останавливаю работу программы')





evm_balance_check()





