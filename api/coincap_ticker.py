import json
import requests

apifile = open('api.txt','r')
apikey = apifile.read().strip() # api key stored here
apifile.close()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

api_headers = {
    'Accepts': 'application/json', # Accepts specifies the type of data returned by the api, in this case its json
    'X-CMC_PRO_API_KEY': apikey   # This parameter takes your api key, so use the api key read from file here
}


limit = 100
start = 1
sort = 'id'
convert = 'USD'

choice = input("Do you want to enter any custom parameters? (y/n): ")

if choice == 'y':
    limit = input('What is the custom limit ?: ')
    start = input('What is the custom start number?: ')
    sort = input('What do you want to sort by?: ')
    convert = input('What is your local currency?: ')

api_url += '&limit=' + limit + '&sort' + sort + '&start=' + start + '&convert=' + convert

res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
result = res.json()

print(json.dumps(result, sort_keys=True, indent=4))
