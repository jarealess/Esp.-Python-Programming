###### DEFINING OUR OWN CLASSES

class Point():
    # pass

    ### definimos un MÉTODO: Es como una función, pero pertenece a una clase
    ### SIEMPRE tiene al menos un argumento: self
    def getX(self):
        return self.x


#### se crean instancias de la clase
point1 = Point()
point2 = Point()


### podemos imprimir (nos muestra el tipo)
print(point1)
print(point1 == point2)

print('\n---------------')
## También podemos agregar variales a cada una de las instancias. 
point1.x = 5
point2.x = 10
print(point1.getX())  ##print(point1.x)
print(point2.getX()) ##print(point2.x)


## 