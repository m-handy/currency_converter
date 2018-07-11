#!C:\Users\martin.hanyas\AppData\Local\Programs\Python\Python36\python.exe

import cgi
import cgitb
import json
import sys
sys.path.append('../')
from base import currency_converter_base as CC

#header
print("Content-Type: application/json")
print("")

amount = None
input_c = None
output_c = None
warning = None

arguments = cgi.FieldStorage()
for i in arguments.keys():
    if i == 'amount':
        amount = float(arguments[i].value)
        continue   
    if i == 'input_currency':
        if arguments[i].value in CC.supported_currencies+CC.supported_signs:
            input_c = arguments[i].value
        else:
            print(json.dumps({'error' : "unsupported currency", 
                            "supported currencies & symbols" : CC.supported_currencies+CC.supported_signs}))
            sys.exit()
        continue
    if i == 'output_currency':
        if arguments[i].value in CC.supported_currencies+CC.supported_signs:
            output_c = arguments[i].value
        else:
            warning = "unsupported output currency"
        continue

if(not amount):
    print("missing amount")
    print("")

if(not input_c):
    print("missing input currency")
    print("")

output_dict = CC.convert(amount, input_c, output_c)
if warning:
    print(json.dumps({'warning': warning, 'input': {'amount':amount, 'currency':CC.translate(input_c)}, 'output': output_dict}, indent=4))
else:
    print(json.dumps({'input': {'amount':amount, 'currency':CC.translate(input_c)}, 
                    'output': output_dict}, sort_keys=True, indent=4))
