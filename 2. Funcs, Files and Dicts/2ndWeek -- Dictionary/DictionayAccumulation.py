#### DICTIONARY ACCUMULATION
with open('flatFile.txt', 'r') as FlatFile:
    texto1 = FlatFile.read()

## contamos la cantidad de a's y e's que aparecen en el texto y se almacena el resultado en un diccionario.

print("------>>>>> A's and E's count <<<<<<<--------")
mydict={}

# se inicilizan las claves
mydict['a'] = 0
mydict['e'] = 0

# se itera para contar
for c in texto1:
    if c == 'a':
        mydict['a'] = mydict['a'] + 1
    elif c == 'e':
        mydict['e'] = mydict['e'] + 1

print("a: " + str(mydict['a']) + " occurrences")
print("e: " + str(mydict['e']) + " occurrences")


### AHORA QUEREMOS CONTAR CADA CARACTER QUE HAYA EN EL TEXTO
print('\n----------->>>>>> Count Every Character Occurrences in the TEXT <<<<<<<<<----------------\n')

## Se inicializa el diccionario y se itera
mydict1 = {}
for c in texto1:
    if c not in mydict1:
        mydict1[c] = 0

    mydict1[c] = mydict1[c] + 1

## se imprimen los resultados
for k, v in mydict1.items():
    print("There are " + str(v) + ' ' + k + "'s in the text")


## MAXIMUN OCURRENCE
print('\nBEST KEY')
print(max(mydict1, key=mydict1.get))