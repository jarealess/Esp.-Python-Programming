### Agregamos parámetros al CONSTRUCTOR
### Es un método que tiene como objetivo inicializar la instancia, incluídas las variables

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

#### se crean instancias de la clase
point1 = Point(5, 10)
point2 = Point(4, 14)

### imprimimos
print(point1.getX())
print(point2.getX())