#!/usr/bin/python3

import urllib.error
import csv

supported_currencies = ['AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR',
                        'ILS','INR','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK',
                        'SGD','THB','TRY','USD','ZAR']
supported_signs = ['лв','R$','₣','¥','Kč','kr','€','£','Kn','Ft','Rp','₪','₨','Kr','¥','₩','RM','₱','zł','L','р.','฿','₤','$','R']

def translate(currency):
    sign_to_currency = {'лв':'BGN', 'R$':'BRL', '₣':'CHF', '¥':'CNY', 'Kč':'CZK', 'kr':'DKK', '€':'EUR', '£':'GBP',
                    'Kn':'HRK', 'Ft':'HUF', 'Rp':'IDR', '₪':'ILS', '₨':'INR', 'Kr':'ISK', '₩':'KRW', 'RM':'MYR', 
                    '₱':'PHP', 'zł':'PLN', 'L':'RON', 'р.':'RUB', '฿':'THB', '₤':'TRY', '$':'USD', 'R':'ZAR'}

    if currency in sign_to_currency:
        return sign_to_currency[currency]
    else:
        return currency


def download_rates(url):
    from urllib.request import urlopen
    from io import BytesIO
    from zipfile import ZipFile

    filename = 'eurofxref.csv'
    response = urlopen(url)
    zipfile = ZipFile(BytesIO(response.read()))
    with open(filename, 'wb') as f:
        for line in zipfile.open(filename).readlines():
            f.write(line)
    return filename

def getrates():
    try:
        # get actual rates online
        filename = download_rates('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
    except urllib.error.URLError:
        # use old revision offline
        filename = 'base/eurofxref.csv'
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',', quotechar='|')
        rows = [r for r in reader]
        rates = dict(zip(rows[0], rows[1]))
        rates.pop('Date')
        rates['EUR'] = 1.0
    return rates

def convert(amount, input_c, output_c):
    input_c = translate(input_c)
    output_c = translate(output_c)
    output_dict = dict()
    rates = getrates()

    if(output_c):
        output_dict[output_c] = round(amount / float(rates[input_c]) * float(rates[output_c]),3)
    else:
        for out_cur in supported_currencies:
            output_dict[out_cur] = round(amount / float(rates[input_c]) * float(rates[out_cur]),3)

    return output_dict

if __name__ == "__main__":
    import sys
    try:
        out_c = sys.argv[3]
    except IndexError:
        out_c = None
    print(convert(float(sys.argv[1]),sys.argv[2],out_c))