import json
import requests

apifile = open('api.txt','r')
apikey = apifile.read().strip() # api key stored here
apifile.close()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

api_headers = {
    'Accepts': 'application/json', # Accepts specifies the type of data returned by the api, in this case its json
    'X-CMC_PRO_API_KEY': apikey   # This parameter takes your api key, so use the api key read from file here
}

res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
result = res.json()

print(json.dumps(result, sort_keys=True, indent=4))

data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')')
