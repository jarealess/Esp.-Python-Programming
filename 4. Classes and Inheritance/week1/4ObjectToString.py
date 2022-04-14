

from tokenize import Pointfloat


class Point():
    ''' Point class for representing and manipulating x,y coordinates'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2)+(self.y ** 2)) ** 0.5

    def __str__(self):
        # cualquier cosa que se ponga aquí será lo que se imprima cuando se llama sin especificar un método
        return f'Point ({self.x}, {self.y})'
            


p = Point(7,6)
print(p)
print(p.distanceFromOrigin())