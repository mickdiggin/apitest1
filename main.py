

import requests
import pprint
import webbrowser
from login import theQueryString, theLogin

url = "https://amazon_data_extractor.p.rapidapi.com/search/"

querystring = theQueryString

headers = theLogin

print("What do you want to search for?")

product = input("> ")

#should probably wrap this in a try-except
response = requests.get((url + product), headers=headers, params=querystring, verify=False)

result = (response.json())

avgPrice = 0

for i in range(0, 10):
	avgPrice += (result['results'][i]['price'])

print(f"The average price for the first 10 items is {round(avgPrice / 10, 2)}.")