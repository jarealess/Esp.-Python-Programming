############################# PODEMOS COMBINAR EXPRESIONES #########################################333
import re


## Queremos matchear una palabra que empiece y termine con A
print(re.search(r'A.*a', 'Me gusta Argentina.'))
print(re.search(r'A.*a', 'Azerbaijan'))

## Imprimió algo con Azerbaijan porque no le especificamos que solo trajera lo que empiece y termine (estrictamente)
print(re.search(r'^A.*a$', 'Azerbaijan'))
print(re.search(r'^A.*a$', 'Australia'))


## Podemos construir una expresión para validar que una variable sea correcta
## NO debe empezar con números, luego de eso puede contener cualquier caracter alfanumérico o _
print('\n------------------------------------')
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
print(re.search(pattern, '_this_is_valid'))
print(re.search(pattern, '00_this_is_not_valid'))
print(re.search(pattern, '_this_is_not_valid()'))
print(re.search(pattern, '_this_is_not_valid()'))