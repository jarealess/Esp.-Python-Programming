## función open para lectura
fileRef = open('datosclientes.txt', 'r')

## lectura
#------ contents = fileRef.read()
#------ print(contents[0:20])  # print(contents)

## lectura2: Para que funcione, se el archivo no debe haber sido leído ya
## Devuelve una lista, cada línea es un elemento
lines = fileRef.readlines()  
for line in lines:
    print(line.strip())


# '../path...' ---> Para buscar un archivo en una ruta partiendo desde el directorio padre


 