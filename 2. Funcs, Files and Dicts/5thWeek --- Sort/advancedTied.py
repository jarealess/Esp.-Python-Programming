states = {'Minesota': ['St. Paul', 'Minneapolis', 'Saint Cloud', 'Stillwater'],
          'Michigan': ['Ann Arbor', 'Traverse City', 'Lansing', 'Kalamazoo'],
          'Washington': ['Seattle', 'Tacoma', 'Olympia', 'Vancouver']}
print(states)

### SI QUEREMOS ORDENAR EL DICCIONARIO POR
print('\n------->>> Ordenado básico')
print(sorted(states))

### SI QUEREMOS ORDENAR POR EL CONTEO DE CIUDADES QUE EMPIEZAN CON S
### SE HACE COMPLICADO TIRARLO CON UNA LAMBA DIRECTA...
print("\n------->>> Ordenado por cantidad de S's iniciales")

### definimos una función que cuente
def count_s_cities(state_list):
    ct = 0
    for city in state_list:
        if city[0]=='S':
            ct+=1
    return ct

### se pasa esto al sorted (recordad que la función definida recibe listas)
print(sorted(states, key=lambda state: count_s_cities(states[state])))


### ordenando por los últimos 4 dígitos
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key=lambda k: str(k)[-4:])
print(sorted_ids)