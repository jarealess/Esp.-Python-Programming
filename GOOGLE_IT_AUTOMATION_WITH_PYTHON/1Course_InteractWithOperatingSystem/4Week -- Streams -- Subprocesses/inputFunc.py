####### EL INPUT

# name = input('Please enter your name: ')
# print('Hola',name)


#### STANDARD STRINGS
# ----> STDIN, STDOUT, STDERR


### ENVIRONMENT VARIABLES
import os

# print('HOME: '+os.environ.get('HOME', ''))
# print('SHELL: '+os.environ.get('SHELL', ''))
# print('FRUIT: '+os.environ.get('FRUIT', ''))


#### SYS ARGV: Nos muestra las variables que le definamos cuando corramos el comando desde bash
import sys
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])