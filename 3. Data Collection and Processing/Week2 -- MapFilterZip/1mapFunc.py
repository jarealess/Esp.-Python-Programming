####### TENEMOS UNA FUNCIÓN QUE TOMA UNA LISTA Y APLICA UNA OPERACIÓN A SUS VALORES

def doubleStuff(list_1):
    new_list = []
    for value in list_1:
        new_list.append(2*value)
    return new_list

lista = [2,5,9]
print(lista)
print(doubleStuff(lista))


########### PODEMOS USAR LA FUNCIÓN MAP PARA APLICAR ESTO A LOS VALORES DE UNA LISTA

### definimos la nueva función
def tiple(value):
    return 3*value

def tripleStuff(list1):
    new_list = list(map(tiple, list1))
    return new_list

def quadrupleStuff(list1):
    new_list = list(map(lambda x: 4*x, list1))
    return new_list

things = [2,5,9]
print('\n----------------')
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)
