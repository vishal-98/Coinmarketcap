import json
import requests

convert = 'USD'

apifile = open('api.txt','r')
apikey = apifile.read().strip() # api key stored here
apifile.close()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
url_end = '?structure=array&convert=' + convert

api_headers = {
    'Accepts': 'application/json', # Accepts specifies the type of data returned by the api, in this case its json
    'X-CMC_PRO_API_KEY': apikey   # This parameter takes your api key, so use the api key read from file here
}


res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
result = res.json()

data = result['data']

ticker_url_pairs = {} # creating a dictionary that stores key values
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

# c print(ticker_url_pairs)

while True:

    print()
    choice = input("Enter the ticker symbol of a cryptocurrency: ")
    choice = choice.upper()

    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' + str(ticker_url_pairs[choice]) + '/' + url_end
    # print(ticker_url)

    res = requests.get(url = ticker_url) # the res variable now has the returned response
    result = res.json()

    # print(json.dumps(result, sort_keys=True, indent=4))

    currency = result['data'][0]

    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = (currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quote = currency['quote'][convert]
    market_cap = quote['market_cap']
    hour_change = quote['percent_change_1h']
    day_change = quote['percent_change_24h']
    week_change = quote['percent_change_7d']
    price = quote['price']
    volume = quote['volume_24h']

    volume_string = '{}'.format(volume)
    market_cap_string = '{}'.format(market_cap)
    circulating_supply_string = '{}'.format(circulating_supply)
    total_supply_string = '{}'.format(total_supply)

    print(str(rank) + ': ' + name + ' (' + symbol + ')')
    print('Market cap: \t\t$' + market_cap_string)
    print('Price: \t\t\t$' + str(price))
    print('24h Volume: \t\t$' + volume_string)
    print('Hour change: \t\t' + str(hour_change) + '%')
    print('Day change: \t\t' + str(day_change) + '%')
    print('Week change: \t\t' + str(week_change) + '%')
    print('Total supply: \t\t' + total_supply_string)
    print('Circulating supply: \t' + circulating_supply_string)
    print('Percentage of coins in circulation: {}'.format( int((circulating_supply / total_supply) * 100)))
    print()
