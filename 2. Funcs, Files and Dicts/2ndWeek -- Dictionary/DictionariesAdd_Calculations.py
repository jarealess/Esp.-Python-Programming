print('First part -- Adding Key-Values\n')
# Definition
dict1 = {}

#Adding key - value pairs
dict1['Uno'] = 'One'
dict1['Dos'] = 'Two'
dict1['Tres'] = 'Three'
print(dict1)

##Another way
dict2 = {'Cuatro':'Four', 'Cinco':'Five', 'Seis':'Six'}
print(dict2)

print('-----------------------------------------------------------------')
print('Dictionay Operations\n')
#Dictionary operations

Inventory = {'apples':430, 'bananas':212, 'oranges':525, 'pears':217}
print(Inventory)

## Deleting
del Inventory['pears']
print('\nDeleting pears')
print(Inventory)

##Changing a Value
Inventory['bananas'] = 0
print('\nChanging value for bananas')
print(Inventory)

## another way
Inventory['bananas'] = Inventory['bananas']+200
print('\nAnother way for changing the value')
print(Inventory)

## Longitug
print('\nLongitud --> len(Inventory) = ' + str(len(Inventory)))

