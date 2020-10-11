import json
import matplotlib.pyplot as plt
import pprint


with open('usdexchangerate.json','r') as f:
    file_currencies = json.loads(f.read())
# New dict creation
rate={}
for currency in file_currencies:
    rate = currency['rates']
# Extracting specific keys and values from dict
Keep_list= ['AUD','CAD','GBP','NZD','SGD'] 
new_dict = dict([(key, val) for key, val in 
           rate.items() if key in Keep_list]) 
#print(new_dict)

# Plotting the grpah
x = new_dict.keys()
y = new_dict.values()
plt.bar(x,y)
plt.xlabel('Name of Currency')
plt.ylabel("Exchange Rate")
plt.title('Exchange Rate for USD in Oct 2020')
plt.show()


"""
#for currency in file_currencies.items():
erates = file_currencies["base"]["rates"])
print(erates)

exchange_rate={} # key is the currency name, value is the exchange rate

for currency in file_currencies:
    currency_name = currency['file_currencies']['rates']
print(currency_name)

#erates = currency['base']['rates']
#print(erates)
#pprint.pprint(file_currencies)
#print(x['base']['rates'])
"""