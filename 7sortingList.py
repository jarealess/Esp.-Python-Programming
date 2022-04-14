#### SE PUEDE ORGANIZAR UNA LISTA DE INSTANCIAS XON SORTED (PASÁNDOLE UN KEY)

from jsonschema import RefResolutionError
from numpy import sort


class Fruit():
    
    printed_rep = 'x' ## Class Variable ----> Se puede usar en los métodos con un Self antes

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sortPriority(self):
        return self.price

L = [Fruit('Apple', 10), Fruit('Banana', 8), Fruit('Blueberry', 15)]
print(sorted(L, key=Fruit.sortPriority))
for f in sorted(L, key=Fruit.sortPriority):
    print(f'{f.name}, {f.price}')
