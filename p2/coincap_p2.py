# Ian Annase
# Mastering The CoinMarketCap API with Python3

import os
import json
import time
import requests
from datetime import datetime

convert = 'USD'

apifile = open('api.txt','r')
apikey = apifile.read()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

api_headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c7a70bdc-dccb-4823-8a4b-4043af850c2c'
}

url_end = '?structure=array&Convert=' + convert

res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
result = res.json()


data = result['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print()
print('ALERTS TRACKING...')
print()

already_hit_symbols = []

while True:
    with open('alerts.txt') as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()
            ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[ticker]) + '/' + url_end

            res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
            result = res.json()

            currency = result['data'][0]
            name = currency['name']
            last_updated = currency['last_updated']
            symbol = currency['symbol']
            quotes = currency['quote'][convert]
            price = quotes['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                os.system('say ' + name + ' hit ' + amount)
                last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')
                print(name + ' hit ' + amount + ' on ' + last_updated_string)
                already_hit_symbols.append(symbol)

    print('...')
    time.sleep(300)
