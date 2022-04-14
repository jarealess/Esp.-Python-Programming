###### EXTRAER INFORMACIÓN DE DOS APIS DISTINTAS
import requests
import json

## api page:  https://tastedive.com/read/api
def get_movies_from_tastedive(key_string):
    paramDict = {'q':key_string, 'type':'movies', 'limit':'5'}
    page = requests.get('https://tastedive.com/api/similar', params=paramDict)
    return page.json()

def extract_movie_titles(key_string):
    resultsList = get_movies_from_tastedive(key_string)['Similar']['Results']
    namesList = [d['Name'] for d in resultsList]
    return namesList

#### PARA UNA LISTA DE PELÍCULAS, NOS MUESTRA LAS RELACIONADAS Y LAS DEJA EN UNA SOLA LISTA
def get_related_titles(list1):
    lst = []
    for movie in list1:
        ### No se usa APPEND sino EXTEND
        lst.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(lst))

#print(extract_movie_titles('iron man'))





##### SEGUNDA API: https://www.omdbapi.com/

def get_movies_from_tastedive(key_string):
    paramDict = {'t':key_string, 'r':'json'}
    page = requests.get('http://www.omdbapi.com/', params=paramDict)
    return page.json()

print(get_movies_from_tastedive('Baby Mama'))