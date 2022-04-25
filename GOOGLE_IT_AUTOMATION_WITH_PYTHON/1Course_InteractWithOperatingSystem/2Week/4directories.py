import os
# https://docs.python.org/3/library/os.html


## Obtener el directorio actual
print(os.getcwd())


## Crear una nueva carpeta
#--- os.mkdir('3Week')


## Cambiar el directorio
#--- os.chdir('.')  #Punto para indicar que vamos al directorio padre
print(os.getcwd())


## Eliminar una carpeta
#--- os.rmdir('3Week')    # Solo funciona si la carpeta está vacía


## Listar los archivos en una carpeta
print(os.listdir('2Week'))

## Mirar si es un directorio
print(os.path.isdir('1Week'))


### CHEQUEAR EL TIPO de los archivos que hay dentro de una carpeta
def check_dir(dir):
    for name in os.listdir(dir):
        fullname = os.path.join(dir, name)
        if os.path.isdir(fullname):
            print(f'{fullname} is a directory')
        else:
            print(f'{fullname} is a file')

check_dir('1Week')