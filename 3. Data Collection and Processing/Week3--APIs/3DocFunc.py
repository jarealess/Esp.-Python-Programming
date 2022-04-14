### Es bueno consultar la documentación de la API para saber cómo funciona todo 
# https://www.datamuse.com/api/


## Es bueno poner todo lo anterior en una función para que quede automático

from email.mime import base
import requests

def get_rhymes(word, max='3'):
    baseUrl = 'https://api.datamuse.com/words'
    params_dict = {}
    params_dict['rel_rhy'] = word
    params_dict['max'] = max

    resp = requests.get(baseUrl, params=params_dict)
    word_ds = resp.json()
    #return [d['word'] for d in word_ds]
    return word_ds

print(get_rhymes('funny'))