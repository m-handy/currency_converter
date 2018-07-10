# currency_converter
## Modules:
- cgi - REST API
- cli - command line tool

## Usage
### CLI
In folder `cli` run f.e. `python .\currency_converter.py --amount 1 --input_currency DKK`
### CGI
Copy folder `cgi` & `base` folder to Apache's `cgi-bin` subfolder.
Example of GET on localhost: `http://localhost/cgi-bin/cgi/currency_converter.py?amount=25.8&input_currency=CZK`