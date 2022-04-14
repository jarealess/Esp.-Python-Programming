import requests

kval_pairs = {'rel_rhy':'funny'}
page = requests.get('https://api.datamuse.com/words', params=kval_pairs)   ## Completa la Url con lo que falte, usando el DICT
print(page.text[0:150])
print(page.url)

##### PODEMOS TENER UNA URL MÁS COMPLICADA
print('\n----------------------------')
d = {'q':'violins and guitars','tbm':'isch'}
results = requests.get('https://google.com/search', params=d)
print(results.url)
print(results.text)
