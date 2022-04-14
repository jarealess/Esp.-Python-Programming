import requests
import json
import ssl

page = requests.get('https://api.datamuse.com/words?rel_rhy=funny')
print(type(page))
print(page.text[:150])
print(page.url)
print('\n-------')
x = page.json()  ## convierte la página en un objeto de python (una lista de diccionarios)
print(type(x))
print('\n first item in the list')
print(x[0])
print('\n the whole list')
print(json.dumps(x, indent=2)) ### pretty printed results