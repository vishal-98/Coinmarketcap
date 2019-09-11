import xlsxwriter
import requests
import json

apifile = open('api.txt','r')
apikey = apifile.read()

api_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

api_headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c7a70bdc-dccb-4823-8a4b-4043af850c2c'
}

start = 1
f = 1

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Day Change')
crypto_sheet.write('H1', 'Week Change')

for i in range(10):
    ticker_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest??structure=array&start=' + str(start)

    res = requests.get(url= api_url , headers = api_headers) # the res variable now has the returned response
    result = res.json()
    data = result['data']


    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quotes = currency['quote']['USD']
        market_cap = quotes['market_cap']
        hour_change = quotes['percent_change_1h']
        day_change = quotes['percent_change_24h']
        week_change = quotes['percent_change_7d']
        price = quotes['price']
        volume = quotes['volume_24h']

        crypto_sheet.write(f,0,name)
        crypto_sheet.write(f,1,symbol)
        crypto_sheet.write(f,2,str(market_cap))
        crypto_sheet.write(f,3,str(price))
        crypto_sheet.write(f,4,str(volume))
        crypto_sheet.write(f,5,str(hour_change))
        crypto_sheet.write(f,6,str(day_change))
        crypto_sheet.write(f,7,str(week_change))

        f += 1

    start += 100

crypto_workbook.close()
