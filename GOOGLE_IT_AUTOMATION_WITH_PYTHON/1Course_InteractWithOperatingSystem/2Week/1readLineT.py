### WITH OPEN cierra el archivo automáticamente, OPEN no lo hace (requeriríamos el file.close() al final)

path = r'C:\Users\PERSONAL\Documents\Especializacion en Analitica\Cursos\Esp.-Python-Programming\GOOGLE_IT_AUTOMATION_WITH_PYTHON\1Course_InteractWithOperatingSystem\2Week'


### De esta manera, se imprime con espacio porque PYTHON agrega un salto de línea, adicional al que ya hay en el archivo.
with open(path+"\spider.txt") as file:
    for line in file:
        print(line.upper())

### SIN SALTO
print('----'*20)

with open(path+"\spider.txt") as file:
    for line in file:
        print(line.strip().upper())
