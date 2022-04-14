##### CON TUPLAS
tups = [('A',3,2), ('C',1,4), ('B',3,1), ('A',2,4), ('C',1,2)]

for tup in sorted(tups):
    print(tup)

print('\n--------')

fruits = ["peach", "kiwi", 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

print('\n------> si queremos cambiar el orden de los empates y general')

fruits = ["peach", "kiwi", 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

print('\n------> si queremos cambiar SOLO el orden de los empates ')
fruits = ["peach", "kiwi", 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, reverse=True, key=lambda fruit_name: (-len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)