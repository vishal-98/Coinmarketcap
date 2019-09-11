import json
import requests

apifile = open('api.txt','r')
apikey = apifile.read()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

api_headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c7a70bdc-dccb-4823-8a4b-4043af850c2c'
}

while True:

    choice = input("Do you want to enter any custom parameters? (y/n): ")

    if choice == 'y':
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

        data = result['data']

        for currency in data:
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
            print('Percentage of coins in circulation: {}'.format( int((circulating_supply / total_supply * 100))))
            print()

    else:
        break
