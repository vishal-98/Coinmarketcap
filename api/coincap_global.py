# import json
# import requests
#
# global_url =  'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
#
#
# request = requests.get(global_url)
# results = request.json()
#
# print(json.dumps(results, sort_keys=True, indent=4))

import json
import requests


# keep your api key in a text file so you dont have to import in code and you can avoid uploading it

# Reading the api key from text file
apifile = open('api.txt','r')
apikey = apifile.read().strip() # api key stored here
apifile.close()
# The url of the api to hit
api_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

# Prepare header for request else your request wont get authenticated
api_headers = {
    'Accepts': 'application/json', # Accepts specifies the type of data returned by the api, in this case its json
    'X-CMC_PRO_API_KEY': apikey   # This parameter takes your api key, so use the api key read from file here
}

# use requests to do get request on the api, specify the url and header for the request
res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response

# extract the data part of res by using res.json() method
result =  res.json()  # result now stores the data sent by the api as a python dictionary for easy access

#coinData = result['data']

# for i in coinData:
#     print(json.dumps(i,indent=4))
# print(json.dumps(result,indent=4,sort_keys=True))

active_currencies = result['data']['active_cryptocurrencies']
active_markets = result['data']['active_market_pairs']
bitcoin_dominance = result['data']['btc_dominance']
last_updated = result['data']['last_updated']
global_cap = int(result['data']['quote']['USD']['total_market_cap'])
global_volume = int(result['data']['quote']['USD']['total_volume_24h'])

active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)

# last_updated_string = datetime.fronttimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

# print()
# print(' There are currently ' + str(active_currencies) + ' active_cryptocurrencies and ' + str(active_markets) + ' active_market_pairs. ')
# print(' The global cap of all the cryptos is ' + str(global_cap) + ' and the 24h global volume is ' + str(global_volume) + '.')
# print(' Bitcoin dominance is ' + str(bitcoin_dominance) + '.')
# print()
# print(' This information was last updated on ' +str(last_updated) + '.')

print()
print(' There are currently ' + active_currencies_string + ' active_cryptocurrencies and ' + active_markets_string + ' active_market_pairs. ')
print(' The global cap of all the cryptos is ' + global_cap_string + ' and the 24h global volume is ' + global_volume_string + '.')
print(' Bitcoin dominance is ' + str(bitcoin_dominance) + '.')
print()
print(' This information was last updated on ' + str(last_updated) + '.')
