import json
import requests
from pprint import pprint
from bs4 import BeautifulSoup
from time import ctime
from datetime import datetime
from datetime import timedelta


version = 'Bitcore webscrapper V2.0.3'

def coingeckoRanking():

                url = 'https://www.coingecko.com/en/coins/bitcore'
                # cssSelector = 'span, class_= "coin-tag mr-1 text-white bg-dark font-weight-bold"'

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                    return

                soup = BeautifulSoup(response.content, 'lxml')
                # saus = soup.find(cssSelector)
                saus =  soup.find("span", class_= "coin-tag mr-1 text-white bg-dark font-weight-bold").text.strip('\n').split('#')[1]
                return f'Ranking #{saus} coingecko.com'

def coinmarketcapRanking():
                try:
                    response = requests.get( 'https://coinmarketcap.com/currencies/bitcore/' )
                    response.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                    return

                soup = BeautifulSoup(response.content, 'lxml')

                saus =  soup.find("span", class_= "cmc-label cmc-label--success sc-13jrx81-0 FVuRP").text.split(' ')[1]
                return f'Ranking #{saus} coinmarketcap.com'

def dolarPrice():
    
                url = 'https://coinmarketcap.com/currencies/bitcore/'

                try:
                    response = requests.get(url)
                    response.raise_for_status()
                except requests.exceptions.HTTPError as err:
                    print(err)
                    return

                soup = BeautifulSoup(response.content, 'lxml')
                price = soup.find("span", class_= "cmc-details-panel-price__price").text
                return price


then = 1588957440.000000
now = datetime.timestamp(datetime.now())

dtThen = datetime.fromtimestamp(then)
dtNow = datetime.fromtimestamp(now)

dtDelta  = dtThen - dtNow
# <div class="et_pb_module et_pb_countdown_timer et_pb_countdown_timer_0 et_pb_bg_layout_dark" data-end-timestamp="1588957440">


# make a functie of this one?
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
coinPrice = dolarPrice().strip('$')
algoDiff = bitcore['difficulty']
algoDiff24 = bitcore['difficulty24']
change_percent = ((float(algoDiff) - algoDiff24) / algoDiff24) * 100

print("*" * 30 + " " +  version + " " +  "*" * 30)
print()
print(f"                     Bitcore core 17.0.0 at {coreProgress}    Algorithm: {bitcore['algorithm']}")
print()
print(f"                               coinmarketcapPrice[BTX] ${coinPrice}")
print()
print(f"            {coingeckoRanking()}     {coinmarketcapRanking()}")
print()
print(f"            Exchange rate: {round(bitcore['exchange_rate']*100000000)} satoshi     Exchange rate 24H: {round(bitcore['exchange_rate24']*100000000)} satoshi")
print()
print()
print(f"                *  Current Difficulty: {algoDiff:3.2f}     NetHash: {netHash:3.2f} Gh/s  *")
print(f"              Average last 24H: {bitcore['difficulty24']:3.2f}    Last 24 hours Change : {change_percent:3.2f}%")
print()
print(f"        Last Block: {bitcore['last_block']}  Timestamp: {bitcore['timestamp']}  Left Supply: {float(btx_data['leftsupply']):3.0f}")  
print()
print(f"                     Block Time: {bitcore['block_time']} Sec.    Reward: {bitcore['block_reward']} BTX/Block")
print(f"                                  Block Reward -50% in {str(dtDelta.days)} days")
print()
print(f" Don't panic! ".center(88,'*'))
print()
input('--+--  key to continue  --+--'.center(90,' '))
