## Agregamos otros métodos a la Clase

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


#### se crean instancias de la clase
point1 = Point(10, 100)


#### printing
print(point1.getX())
print(point1.getY())