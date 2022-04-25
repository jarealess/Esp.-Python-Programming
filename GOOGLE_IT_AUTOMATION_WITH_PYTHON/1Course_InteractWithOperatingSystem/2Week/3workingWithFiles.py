### VAMOS A TRABAJAR CON EL MODULO OS

import os
import datetime

path = r'C:\Users\PERSONAL\Documents\Especializacion en Analitica\Cursos\Esp.-Python-Programming\GOOGLE_IT_AUTOMATION_WITH_PYTHON\1Course_InteractWithOperatingSystem\2Week'

### Eliminar un archivo
#--- os.remove(path+"\\novel.txt")

### Renombrar el archivo
#--- os.rename(path+"\spider.txt", path+'\spider2.txt')

##CHECKEAR si un archivo existe
print(os.path.exists(path+"\spidercito.txt")) 
print(os.path.exists(path+"\spider2.txt")) 


### Más información de los archivos

## Tamaño de archivo
print(os.path.getsize(path+"\spider2.txt")) 

## última modificación
print(os.path.getmtime(path+"\spider2.txt"))  # devuelve la fecha en formato UNIX (segundos desde 01/01/1970)

