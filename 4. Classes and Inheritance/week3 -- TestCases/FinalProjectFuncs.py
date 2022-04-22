#### Algunas funcnciones de importancia

# time.sleep para retrasar la ejecución del código unos segundos que le damos como parámetro. 
import time

from scipy import rand

for x in range(2,6):
    print(f'Sleep {x} seconds...')
    time.sleep(x)
print('Done!\n----------------------------------------------\n')

# random para generar números aleatorios

import random

rand_number = random.randint(1,100)
print(f'Random number between 1 and 100: {rand_number}')

letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
rand_letter = random.choice(letters)
print(f'Random letter {rand_letter}')
print('--------------------------------\n')

# COUNT
myString = 'Hello, World! 123'
print(myString.count('l'))
