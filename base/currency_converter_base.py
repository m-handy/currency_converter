#!/usr/bin/python3

import urllib.error
import csv

supported_currencies = ['AUD','BGN','BRL','CAD','CHF','CNY','CZK','DKK','EUR','GBP','HKD','HRK','HUF','IDR',
                        'ILS','INR','ISK','JPY','KRW','MXN','MYR','NOK','NZD','PHP','PLN','RON','RUB','SEK',
                        'SGD','THB','TRY','USD','ZAR']
supported_signs = ['лв','R$','₣','¥','Kč','kr','€','£','Kn','Ft','Rp','₪','₨','Kr','¥','₩','RM','₱','zł','L','р.','฿','₤','$','R']

def translate(currency):
    currency_signs = {'лв':'BGN', 'R$':'BRL', '₣':'CHF', '¥':'CNY', 'Kč':'CZK', 'kr':'DKK', '€':'EUR', '£':'GBP',
                    'Kn':'HRK', 'Ft':'HUF', 'Rp':'IDR', '₪':'ILS', '₨':'INR', 'Kr':'ISK', '₩':'KRW', 'RM':'MYR', 
                    '₱':'PHP', 'zł':'PLN', 'L':'RON', 'р.':'RUB', '฿':'THB', '₤':'TRY', '$':'USD', 'R':'ZAR'}

    if currency in currency_signs:
        return currency_signs[currency]
    else:
        return currency

def convert(amount, input_c, output_c):
    input_c = translate(input_c)
    output_c = translate(output_c)
    #http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip
    with open('base/eurofxref.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',', quotechar='|')
        rows=[r for r in reader]
        mydict = dict(zip(rows[0], rows[1]))
        mydict.pop('Date')
        mydict['EUR'] = 1.0
        output_dict = dict()
        if(output_c):
            output_dict[output_c] = round(amount / float(mydict[input_c]) * float(mydict[output_c]),3)
        else:
            for out_cur in supported_currencies:
                output_dict[out_cur] = round(amount / float(mydict[input_c]) * float(mydict[out_cur]),3)

    return output_dict

if __name__ == "__main__":
    import sys
    try:
        out_c = sys.argv[3]
    except IndexError:
        out_c = None
    print(convert(float(sys.argv[1]),sys.argv[2],out_c))