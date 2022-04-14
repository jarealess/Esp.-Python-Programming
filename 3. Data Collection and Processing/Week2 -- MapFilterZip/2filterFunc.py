########### FILTRO LARGO, NÚMEROS PARES
def keep_evens(numList):
    new_list = []
    for num in numList:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3,4,6,7,0,1]))

###########FILTRO CON FILTER
print('\n----------------')

def keep_evens2(numList):
    new_list = list(filter(lambda num: num % 2 == 0, numList))
    return new_list

print(keep_evens2([3,4,6,7,0,1]))
