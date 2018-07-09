#!/usr/bin/python3

import argparse
import urllib.error
import json
from currency_converter import CurrencyConverter

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

parser = argparse.ArgumentParser()
parser.add_argument("--amount", action="store", type=float, required=True)
parser.add_argument("--input_currency", action="store", required=True, choices=supported_currencies+supported_signs)
parser.add_argument("--output_currency", action="store", choices=supported_currencies+supported_signs)
args = parser.parse_args()

try:
    c = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
except urllib.error.URLError:
    c = CurrencyConverter()

input_dict = {'amount':args.amount, 'currency':translate(args.input_currency)}
output_dict = dict()

if(args.output_currency):
    output_dict[translate(args.output_currency)] = c.convert(input_dict['amount'], input_dict['currency'], translate(args.output_currency))
else:
    for out_cur in supported_currencies:
        output_dict[out_cur] = c.convert(input_dict['amount'], input_dict['currency'], out_cur)

print(json.dumps({'input': input_dict, 'output': output_dict}, sort_keys=True, indent=4))



