import requests
from sys import exit


baseurl = "https://api.fixer.io/"
base_currency = "base="+(input("Enter the code for base currency (default Euro): ") or 'EUR')


if input("Do you want to get exchange rates for all the currency? (Y/N) ") == 'Y':
    json = requests.get(baseurl+"latest?"+base_currency).json()
    print("Priting exchange rates against", json['base'])
    rates = sorted(json['rates'].keys())
    for rate in rates:
        print(rate, json['rates'][rate])
    exit()


curr = input("Enter the code for the currency to want to get rates: ")
if input("Get lates rates (Y/N): ") == 'Y':
    json = requests.get(baseurl+"latest?"+base_currency+"&symbols="+curr).json()
    print(curr+"vs"+json['base'], json['rates'][curr])
    exit()
