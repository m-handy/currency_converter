#!C:\Users\martin.hanyas\AppData\Local\Programs\Python\Python36\python.exe
import cgi
import cgitb
import json
import base.currency_converter_base as CC

#header
print("Content-Type: application/json")
print("")

amount = None
input_c = None
output_c = None

arguments = cgi.FieldStorage()
for i in arguments.keys():
    if i == 'amount':
        amount = float(arguments[i].value)
        continue   
    if i == 'input_currency':
        input_c = arguments[i].value
        continue
    if i == 'output_currency':
        output_c = arguments[i].value
        continue

if(not amount):
    print("missing amount")
    print("")

if(not input_c):
    print("missing input currency")
    print("")

output_dict = CC.convert(amount, input_c, output_c)
print(json.dumps({'input': {'amount':amount, 'currency':CC.translate(input_c)}, 
                'output': output_dict}, sort_keys=True, indent=4))
