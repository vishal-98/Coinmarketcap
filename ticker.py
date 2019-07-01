import json
import requests

apifile = open('api.txt','r') 
apikey = apifile.read()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

api_headers = {
    'Accepts': 'application/json', 
    'X-CMC_PRO_API_KEY': apikey   
}

start = input('Start at : ')
limit = input('Custom limit : ')
sort = input('Sort type : ')
convert = input('Convert to : ')

parameters = {
    'start' : start,
    'limit' : limit,
    'sort' : sort,
    'convert' : convert
}

res = requests.get(url= api_url, params=parameters, headers = api_headers)

result = res.json()

print(json.dumps(result,indent=2))
