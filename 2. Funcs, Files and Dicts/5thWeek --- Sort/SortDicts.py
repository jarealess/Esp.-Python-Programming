L = ['E', 'F', 'B', 'A', 'D', 'I', 'I', 'C', 'B', 'A', 'D', 'D', 'E', 'D']

## Creamos el diccionario con las frecuencias
myDict = {}
for x in L:
    if x not in myDict:
        myDict[x]=0
    myDict[x]+=1

print(myDict)

print('\n------')
for x in sorted(myDict.keys()):
   print(f'{x} appears {myDict[x]} times')

print('\n------')
for x in sorted(myDict.keys(), reverse=True, key=lambda k: myDict[k]):
   print(f'{x} appears {myDict[x]} times')
  
