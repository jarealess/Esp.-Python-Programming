##SEGUNDO PARÁMETRO DEL WITH OPEN('', param)
# 'r': read only
# 'w': write only
# 'a': append
# 'r+': read-write
# 'x': Creación -- Falla si ya existe

### Si el archivo YA EXISTE y lo abrimos con Write-Only, todo su contenido SE BORRA
### Si queremos agregar contenido, sin borrar, debemos abrirlo con 'a' o 'r+'

path = r'C:\Users\PERSONAL\Documents\Especializacion en Analitica\Cursos\Esp.-Python-Programming\GOOGLE_IT_AUTOMATION_WITH_PYTHON\1Course_InteractWithOperatingSystem\2Week'

with open(path+"\spider.txt", 'a') as file:
    file.write('\nThis is a new line...')