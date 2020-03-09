import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from time import ctime
from datetime import datetime
from datetime import timedelta

version = 'Bitcore webscrapper V2.0.1'
myBtx = 1580.190732681

then = 1588957440.000000
now = datetime.timestamp(datetime.now())

dtThen = datetime.fromtimestamp(then)
dtNow = datetime.fromtimestamp(now)

dtDelta  = dtThen - dtNow


# <div class="et_pb_module et_pb_countdown_timer et_pb_countdown_timer_0 et_pb_bg_layout_dark" data-end-timestamp="1588957440">


response = requests.get('https://bitcore.cc/')

# <span class="et_pb_counter_amount_number_inner">87%</span>
soup = BeautifulSoup(response.content, 'lxml')
saus = soup.select('span .et_pb_counter_amount_number_inner')[3]

coreProgress = saus.getText()
print ()


header = {'Content-Type':  'application/json; charset=utf-8'}
urlApi = 'http://bitcore.cc/api.php'

response = requests.get(urlApi, headers=header)
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

#coinCap = b['data']
#coinPrice = coinCap['quotes']['USD']
algoDiff = bitcore['difficulty']
algoDiff24 = bitcore['difficulty24']
change_percent = ((float(algoDiff) - algoDiff24) / algoDiff24) * 100

print("*" * 30 + " " +  version + " " +  "*" * 30)
print()
print(f"                   Bitcore core 17.0.0 at {coreProgress}    Algorithm: {bitcore['algorithm']}")
print()
# print(f"              Price[{coinCap['symbol']}] ${coinPrice['price']:3.2f}     Rank: {coinCap['rank']}     Market_cap: {bitcore['market_cap']}")
print()
print(f"            Exchange rate: {round(bitcore['exchange_rate']*100000000)} satoshi     Exchange rate 24H: {round(bitcore['exchange_rate24']*100000000)} satoshi")
print()
print()
print(f"                *  Current Difficulty: {algoDiff:3.2f}     NetHash: {netHash:3.2f} Gh/s  *")
print(f"              Average last 24H: {bitcore['difficulty24']:3.2f}    Last 24 hours Change : {change_percent:3.2f}%")
print()
print(f"           Last Block: {bitcore['last_block']}  Timestamp: {bitcore['timestamp']}  Left Supply: {float(btx_data['leftsupply']):3.2f}")  

#print(f"     Maximum: {coinCap['max_supply']}  Total: {coinCap['total_supply']}  Circulating: {coinCap['circulating_supply']}\n")
#print(f"     Airdrop: {float(btx_data['airdrop']):3.2f} Virtual Fork: {float(btx_data['vfork']):3.2f}  Claimed: {float(btx_data['claimed']):3.2f}")
#print(f"    Mining: {float(btx_data['mining']):3.2f}  Marketing: {float(btx_data['marketing']):3.2f}  Circulating: {float(btx_data['circulating']):3.2f}")

print()
print(f"                     Block Time: {bitcore['block_time']} Sec.    Reward: {bitcore['block_reward']} BTX/Block")

print(f"                                  Block Reward -50% in {str(dtDelta.days)} days")
# print("                             Block half Time!: " + ctime(1588957440))
print()
# print(f" Don't panic! ${myBtx * coinPrice['price']:3.2f} ".center(86,'*'))
print(f" Don't panic! ".center(88,'*'))

input('\n                            --+--  key to continue  --+--')
