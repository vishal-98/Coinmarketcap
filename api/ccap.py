import json
import requests

# keep your api key in a text file so you dont have to import in code and you can avoid uploading it

# Reading the api key from text file
apifile = open('api.txt','r')
apikey = apifile.read().strip() # api key stored here
apifile.close()
# The url of the api to hit
api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Prepare header for request else your request wont get authenticated
api_headers = {
    'Accepts': 'application/json', # Accepts specifies the type of data returned by the api, in this case its json
    'X-CMC_PRO_API_KEY': apikey   # This parameter takes your api key, so use the api key read from file here
}

# use requests to do get request on the api, specify the url and header for the request
res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response

# extract the data part of res by using res.json() method
result =  res.json()  # result now stores the data sent by the api as a python dictionary for easy access

coinData = result['data']

for i in coinData:
    if i['name'] == 'Bitcoin':
        print(json.dumps(i,indent=4))
        print(i['quote']['USD']['price'])

# print(json.dumps(coinData,indent=4)) # printing the result
