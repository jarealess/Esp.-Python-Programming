#####LISTAS ANIDADAS
list1 = [['a', 'b', 'c'], ['d', 'e'], ['f','g','h']]

## imprimimos primera sublista
print(list1[0])

## agregar otra lista
list1.append(['i'])
print(list1)

## podemos iterar
for l in list1:
    print(l)


####>>>SE PUEDE AGREGAR VALORES NUEVOS A CADA SUBLISTA<<<<!!!!!!
print('\n-------->>>> Se agregan valores a sublistas 0 y 1<<<<<----------')
list1[0].append('z')
list1[1].append('w')
print(list1)


###>>> Imprimiendo valor de una sublista 
print('\n-----tercer valor segunda sublista-------')
print(list1[1][2])

### >> podemos cambiar el valor de alguna posición de la lista
print('\n------Reemplazo del primer valor, tercera sublista------')
list1[2][0] = 'JANICK'
print(list1)


########### DICCIONARIOO ANIDADO DENTRO DE LISTA #########
print('\n\n----->>>>>NESTED DICTIONARIES<<<<<<<<<<<<------')
list2 = [{'a':1, 'b':2, 'c':3}, {'a':5, 'c':90, 5:50}]
print(list2)
print('\n')

## valor de 'b'
print(list2[0]['b'])
print(list2[1].items())