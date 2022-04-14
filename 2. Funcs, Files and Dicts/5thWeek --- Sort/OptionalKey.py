##### PODEMOS AGREGAR UN PARÁMETRO EXTRA A LA FUNCIÓN SORTED PARA ORDENAR
##### ESTE PARÁMETRO PUEDE SER UNA FUNCIÓN PREVIAMENTE DEFINIDA.... SE PASA AL ARGUMENTO >>> KEY <<<<

L1 = [1,7,-2,3,-6]

## definimos la función
def absolute(x):
    if x>=0:
        return x
    else:
        return -x


print(sorted(L1))
print(sorted(L1, key=absolute))
print(sorted(L1, reverse=True, key=absolute))


#### También podemos llamar una LAMBDA
print("-------------")
print(sorted(L1, key=lambda x: absolute(x)))