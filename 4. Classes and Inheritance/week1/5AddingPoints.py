### PODEMOS AGREGAR DOS LLAMADAS A LA CLASE


class Point():
    ''' Point class for representing and manipulating x,y coordinates'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # cualquier cosa que se ponga aquí será lo que se imprima cuando se llama sin especificar un método
        return f'Point ({self.x}, {self.y})'
    
    def __add__(self, otherPoint):
        ### se define el método con __  (esta parece ser una de las claves)
        return Point(self.x + otherPoint.x,
                        self.y + otherPoint.y)
    
    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                        self.y - otherPoint.y)

p1 = Point(-5,10)
p2 = Point(15,20)
print(p1)
print(p2)
print(p1+p2)
print(p1-p2)