####################################### CAPTURING GROUPS ##################################################################3
import re

from pkg_resources import resource_listdir

### Son porciones del patrón que están encerradas entre paréntesis
pattern = '^(\w*), (\w*)$'
result = re.search(pattern, 'Lovelace, Adan')
print(result)
print(result.groups())    ### Grupos >> Imprime Tupla >> Podemos accederla con índices
print(result[0])
print(result[1])
print(result[2])


#### Podemos usar lo anterior por ejemplo para organizar nombres....
def rearrange_name(name):
     pattern = '^(\w*), (\w*)$'
     result = re.search(pattern, name)
     
     if result is None:
         return name
     return f'{result[2]} {result[1]}'

print('\n----------------------------------------')
print(rearrange_name('Lovelace, Adan'))
print(rearrange_name('Ritchie, Dennis'))
print(rearrange_name('Hopper, Grace M.'))   ## No lo matchea

### La definimos nuevamente
def rearrange_name2(name):
     pattern = '^([\w .-]*), ([\w .-]*)$'
     result = re.search(pattern, name)
     
     if result is None:
         return name
     return f'{result[2]} {result[1]}'

print('\n----------------------------------------')
print(rearrange_name2('Hopper, Grace M.')) 


############################################## MORE ON REPETITION QUALIFIERS ###################################################


### Para matchear cualquier string de 5 letras
print('\n----------------------------------------')
print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
print(re.search(r'[a-zA-Z]{5}', 'a scary ghost appeared'))
print(re.findall(r'[a-zA-Z]{5}', 'a scary ghost appeared')) ## matchea las primeras 5 de la última palabra

### Para matchear cualquier string de 5 letras exactamente (USAMOS \b)
print('\n----------------------------------------')
print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))

### Podemos decirle que haga Match a los caracteres en cierto rango
print('\n----------------------------------------')
print(re.findall(r'\w{5,10}', 'I really like strawberries'))
print(re.findall(r'\w{5,}', 'I really like strawberries'))  ## el límte inf/sup se puede dejar abierto
print(re.findall(r'\b[a-zA-Z]{,5}\b', 'I really like strawberries'))  ## el límte inf/sup se puede dejar abierto



############################################## EXTRACTING PID WITH REGREX ###################################################

print('\n----------------------------------------')
pattern = r'\[(\d+)\]'
result = re.search(pattern, 'A different string [34567]')
print(result[0])
print(result[1])



############################################## SPLIT AND REPLACING ###################################################

print('\n----------------------------------------')
print(re.split(r'[.?!]', 'One sentence. Another one? And the last one!'))
print(re.split(r'([.?!])', 'One sentence. Another one? And the last one!'))


## Si queremos sustituir un STRING, podemos hacerlo con SUB
print('\n----------------------------------------')
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'Received and email from go_nuts@my.example.com'))

## Podemos usar SUB para hacer lo de organizar los nombre...
print('\n----------------------------------------')
print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada'))

