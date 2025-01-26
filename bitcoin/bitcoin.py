import requests
import sys

#Expects the user to specify as a command-line argument the number of Bitcoins, 
#If that argument cannot be converted to a float, 
# the program should exit via sys.exit with an error message.
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

#Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, 
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. 
# Be sure to catch any exceptions, as with code like:
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

bitcoin_price = r['bpi']['USD']['rate_float']
amount_btc = bitcoins * bitcoin_price

print(f"${amount_btc:,.4f}")


