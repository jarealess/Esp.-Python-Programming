###...............

L1 = [3,4,5]
L2 = [1,2,3]
L3 = []

for i in range(len(L1)):
    L3.append((L1[i],L2[i]))

print(L3)


### ZIP: CREA UNA LISTA DE TUPLAS
print('\n-------------')
L4 = list(zip(L1,L2))
print(L4)

### podemos iterarlo
print('\n-------------')
for (val1,val2) in L4:
    print(val1+val2)

### SE PUEDE USAS LIST_COMPREHENSION
print('\n-------------')
L5 = [val1+val2 for (val1,val2) in list(zip(L1,L2))]
print(L5)



##### ejercicios
print('\n-------------')
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = [(val1,val2) for (val1,val2) in list(zip(l1,l2)) if len(val1) > 3 and len(val2) > 3] 
opposites2 = list(filter(lambda x: len(x[1]) > 3 and len(x[0]) > 3, list(zip(l1,l2))))
print(opposites2)
