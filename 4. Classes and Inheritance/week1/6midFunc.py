#### PODEMOS AGREGAR OTRA FUNCIÓN PARA ENCONTRAR EL PUNTO MEDIO ENTRE DOS INGRESADOS


class Point():
    ''' Point class for representing and manipulating x,y coordinates'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def halfway(self, target):
        mx = (self.x + target.x)/2 
        my = (self.y + target.y)/2

        return Point(mx, my)

    def __str__(self):
        # cualquier cosa que se ponga aquí será lo que se imprima cuando se llama sin especificar un método
        return f'x = {self.x}, y = {self.y}'
 
p = Point(3,4)
q = Point(5,12)

mid = p.halfway(q)
print(mid)
print(mid.x)
print(mid.y)
