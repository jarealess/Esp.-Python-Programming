import json

a_string = '\n\n\n {\n "resultCount":25,\n "results":[\n\t{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]\n\t}'
print(a_string)

print('-----------')
#### USAMOS LA FUNCIÓN LOADS PARA CONVERTIR EL STRING EN UN DICCIONARIO
d = json.loads(a_string)
print(type(d))
print(d.keys())
print(d['results'])

print('\n-----------')
#### función DUMPS para hacer lo contrario
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

d = {'key': {'c':2, 'a':4, '5':50}, 'key2': {'b':3, 'c':'yes'}}
print(d)
print('\n------')
print(pretty(d))