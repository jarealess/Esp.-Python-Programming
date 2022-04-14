#### SE PUEDE TENER UNA LISTA COMPUESTA DE FUNCIONES, QUE PODEMOS LLAMAR Y UTILIZAR

## primera función
def square(x):
    return x*x

## lista
L = [square, abs, lambda x: x+1]

## se imprimen las funciones contenidas en la lista
print('*****Functions names******')
for f in L:
    print(f)


## se pueden utilizar dichas funciones
print('\n***** se aplican las funciones al valor -2*********')
for f in L:
    print(f(-2))

### podemos llamar solo una de las funciones
print('\n---------')
print(L[2](3))