################ ITUNES
# https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api

import requests
import json

params = {'term':'Ann Arbor', 'entity':'podcast'}
iTunesResponse = requests.get('https://itunes.apple.com/search', params=params)
#print(iTunesResponse.text[:150])
x = iTunesResponse.json()
print(type(x))
print(json.dumps(x, indent=2))
