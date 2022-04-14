### Es una forma de hacer Map o Filter de manera más óptima

### MAP
things = [2,5,9]
yourlist = [x*2 for x in things]
print(yourlist)


### FILTER
def keep_evens(numList):
    new_list = [num for num in numList if num % 2 == 0]
    return new_list

print('\n------------')
print(keep_evens([3,4,6,7,8,0,1]))