import json
import requests
from requests.exceptions import HTTPError
from pprint import *
from time import sleep

header = {'Content-Type':  'application/json; charset=utf-8'}

urlApi = 'http://bitcore.cc/api.php'

try:
    response = requests.get(urlApi, headers=header)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
    sleep(10)
    exit()
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
    exit()

a = json.dumps(response.json())    # dump response to a as a string
b = json.loads(a)              # decode json format b

btx_data = b["data"]

# Get info from second website...  http://whattomine.com
urlApi = 'http://whattomine.com/coins.json'
response = requests.get(urlApi, headers=header)
a = json.dumps(response.json())    # dump response to a
b = json.loads(a)                  # decode json format b

coins = b["coins"]
bitcore = (coins["Bitcore"])
netHash = bitcore['nethash'] / 1000000000

# Bitcore BTX information from https://api.coinmarketcap.com/
urlApi = 'https://api.coinmarketcap.com/v2/ticker/1654/'
response = requests.get(urlApi, headers=header)

# String
a = json.dumps(response.json())    # dump response to a
# Dict
b = json.loads(a)                  # decode json format b

# print(type(a))
# pprint(a)
# print(type(b))
# pprint(b['data'])
# pprint(b.keys())

coinCap = b['data']
coinPrice = coinCap['quotes']['USD']
algoDiff = bitcore['difficulty']
algoDiff24 = bitcore['difficulty24']
change_percent = ((float(algoDiff) - algoDiff24) / algoDiff24) * 100

print("")
print("*" * 28 + " Mantronix Rules! " + "*" * 28)
print(f"            Name:  {coinCap['name']} [{coinCap['symbol']}]   -   Algorithm  : {bitcore['algorithm']}\n")
print(f"         Market_cap: {bitcore['market_cap']}   Price[{coinCap['symbol']}] ${coinPrice['price']:3.2f}   Rank: {coinCap['rank']}")
print(f"      Exchange rate: {round(bitcore['exchange_rate']*100000000)} satoshi   Exchange rate 24H: {round(bitcore['exchange_rate24']*100000000)} satoshi\n")
print(f"             Block Time: {bitcore['block_time']} Sec. - Reward: {bitcore['block_reward']} BTX/Block")
print(f"      Last Block: {bitcore['last_block']}  Timestamp: {bitcore['timestamp']} Left Supply: {float(btx_data['leftsupply']):3.2f}\n")
print(f"           *  Current Difficulty: {algoDiff:3.2f}  NetHash: {netHash:3.2f} Gh/s  *\n")
print(f"     Maximum: {coinCap['max_supply']}  Total: {coinCap['total_supply']}  Circulating: {coinCap['circulating_supply']}\n")
print(f"     Airdrop: {float(btx_data['airdrop']):3.2f} Virtual Fork: {float(btx_data['vfork']):3.2f}  Claimed: {float(btx_data['claimed']):3.2f}")
print(f"    Mining: {float(btx_data['mining']):3.2f}  Marketing: {float(btx_data['marketing']):3.2f}  Circulating: {float(btx_data['circulating']):3.2f}")
print(f"        Average last 24H: {bitcore['difficulty24']:3.2f}  Last 24 hours Change : {change_percent:3.2f}%")
print("*" * 74)

input('\n                       --+--  key to continue  --+--')
