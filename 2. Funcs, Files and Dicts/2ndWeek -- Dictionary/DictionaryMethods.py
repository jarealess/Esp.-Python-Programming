Inventory = {'apples':430, 'bananas':212, 'oranges':525, 'pears':217}

## loop over the keys
print('---------->> Printing keys <<---------')
for key in Inventory.keys():
    print(key)

print('\n----->> Print asociated value <<--------')
for key in Inventory.keys():
    print(key, 'has the value', Inventory[key])


## We could get a list of keys
print('\n---->> Getting List of Keys <<-----')
keys = list(Inventory.keys())
print(keys)

## To print values
print('\n--->> Printing just values <<----')
print(list(Inventory.values()))

print('\n--->> Printing items <<----')
print(list(Inventory.items()))


### LOGICAL VALUES 
print('\n ---------->>>>>>>>> LOGICAL COMPARISSONS <<<<<<<<<<------------')
print('\napples in Inventory?')
print('apples' in Inventory)

print('\ncherries in Inventory?')
print('cherries' in Inventory)


### IF / ELSE
print('\nIs there "bananas" in Inventory? What is the value?')
if 'bananas' in Inventory:
    print(Inventory['bananas'])
else:
    'We have no bananas'


### GET
print('\nInventory.get("apples")', Inventory.get('apples'))


### INTERARING OVER KEY AND VALUE
print('\ndict.items() to iterate over key and value')
for k, v in Inventory.items():
    print(k,':',v)