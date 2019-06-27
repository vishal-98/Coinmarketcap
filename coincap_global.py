import json
import requests

global_url =  'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'


request = requests.get(global_url)
results = request.json()

print(json.dumps(results, sort_keys=True, indent=4))

# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

# import requests
# import json
#
#
# url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
# parameters = {
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'c7a70bdc-dccb-4823-8a4b-4043af850c2c',
# }
# results = request.json()
# results.headers.update(headers)
#
# try:
#   response = results.get(url, params=parameters)
#   data = json.loads(response.text)
#   print(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)
