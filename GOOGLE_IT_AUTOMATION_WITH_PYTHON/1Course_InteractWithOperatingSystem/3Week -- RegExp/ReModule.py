#### Podemos usar expresiones regulares para extraer información de acuerdo a un patrón
import re

## Queremos extraer los dígitos entre corchetes en el siguiente texto
log = 'July 31 07:51:18 mycomputer bad_process[12345]: ERROR Performing package upgrade'
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1])


#### Cuando no hace match, retorna None
result = re.search(r'aza', 'maze')
print(result)


### Matcheando caracteres especiales
print(re.search(r'^x', 'xenon'))  # Match si la palabra empieza con X
print(re.search(r'^x', 'matrix'))


## El punto matchea cualquier caracter
print(re.search(r'p.ng', 'penguin'))
print(re.search(r'p.ng', 'sponge'))
print(re.search(r'p.ng', 'clapping'))


### Podemos decirle que ignore mayúscula o minúscula
print(re.search(r'p.ng', 'Pangea'))
print(re.search(r'p.ng', 'Pangea', re.IGNORECASE))


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WILDCARS AND CHARACTERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('\n------------------------------------')

## [] Nos permite matchear basado en lo que dejemos dentro
print(re.search(r'[Pp]ython', 'Python'))
print(re.search(r'[Pp]ython', 'python'))


### [a-z] para match de cualquier letra 
print(re.search(r'[a-z]way', 'The end of the highway'))
print(re.search(r'[a-z]way', 'I always loved pizza'))
print(re.search(r'[a-z]way', 'What a way to go'))  ### ninguna letra antes

### ([A-Z] para mayúsculas, [0-9] para dígitos)
print('\n------------------------------------')
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudy'))
print(re.search(r'cloud[a-zA-Z0-9]', 'cloud9'))


### [^] para decirle que NO matchee lo siguiente
print('\n------------------------------------')
print(re.search(r'[^a-zA-Z]', 'A sentence with spaces.')) ## Matchea el primer espacio

## Podemos agregar ESPACIO a los caracteres que no queremos matchear
print(re.search(r'[^a-zA-Z ]', 'A sentence with spaces.'))  ##matchea el punto


## | para matchear uno u otro caracter
print('\n------------------------------------')
print(re.search(r'cat|rep', 'caterpilar'))
print(re.search(r'cat|rep', 'reptile'))
print(re.search(r'cat|dog', 'I love cats and dogs')) ## solo matchea la primera coincidencia


###  FINDALL para que haga match a todo lo que encuentre 
print('\n------------------------------------')
print(re.findall(r'cat|dog', 'I love cats and dogs'))


### FINDALL para que haga match a todo lo que encuentre 
print('\n------------------------------------')


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REPETITION QUALIFIERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

## * para hacer match a un caracter 0 o más veces
print(re.search(r'Py.*n', 'Python'))  ## Matchea 'Py', seguido por n-caracteres, seguido por 'n'
print(re.search(r'Py.*n', 'Pygmalion'))
print(re.search(r'Py.*n', 'Python Programming'))   ### <<<<--------

### Si quisieramos que solo matcheara las letras (no el espacio):
print(re.search(r'Py[a-z]*n', 'Python Programming')) 
print(re.search(r'Py[a-z]*n', 'Pyn')) 


## + para hacer match a un caracter 1 o más veces
print('\n------------------------------------')
print(re.search(r'Py[a-z]+n', 'Pyn')) 
print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woolly'))
print(re.search(r'o+l+', 'boil'))  ## No matchea porque o y l no están juntas


## ? para hacer match a un caracter 0 o 1 vez
print('\n------------------------------------')
print(re.search(r'p?each','The each their own'))
print(re.search(r'p?each','I like peaches'))


###>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ESCAPING CHARACTERS <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

## Si queremos buscar un string que tenga un . (requerimos el escape)
print('\n------------------------------------')
print(re.search(r'.com','welcome'))
print(re.search(r'\.com','welcome'))
print(re.search(r'\.com','mydomain.com'))


### \w para matchear cualquier caracter alfanumérico y _
print('\n------------------------------------')
print(re.search(r'\w*', 'This is an example'))
print(re.search(r'\w*', 'And_this_is_another'))

#### \d para dígitos, \s para espacios,  \b para word boundaries