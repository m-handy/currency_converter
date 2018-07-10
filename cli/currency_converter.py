#!C:\Users\martin.hanyas\AppData\Local\Programs\Python\Python36\python.exe

import argparse
import json
import sys
sys.path.append('../')
from base import currency_converter_base as CC

parser = argparse.ArgumentParser()
parser.add_argument("--amount", action="store", type=float, required=True)
parser.add_argument("--input_currency", action="store", required=True, choices=CC.supported_currencies+CC.supported_signs)
parser.add_argument("--output_currency", action="store", choices=CC.supported_currencies+CC.supported_signs)
args = parser.parse_args()

output_dict = CC.convert(args.amount, args.input_currency, args.output_currency)

print(json.dumps({'input': {'amount':args.amount, 'currency':CC.translate(args.input_currency)}, 
                'output': output_dict}, sort_keys=True, indent=4))