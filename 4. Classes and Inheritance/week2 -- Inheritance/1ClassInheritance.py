#### Una clase puede heredar los métodos y variables de otras


class Person():
    CURRENT_YEAR = 2022
    
    def __init__(self, name, yearBorn):
        self.name = name
        self.yearBorn = yearBorn

    def getAge(self):
        return self.CURRENT_YEAR - self.yearBorn

    def __str__(self):
        return '{} ({})'.format(self.name, self.getAge())


alice = Person('Alice Smith', 1995)
print(alice)




############ La segunda clase se define poniendo como "argumento" la primera

class Student(Person):
    def __init__(self, name, yearBorn):
        #### se llama el constructor de la clase anterior
        Person.__init__(self, name, yearBorn)
        self.knowlegde = 0
    
    ## solo es necesario definir los nuevos métodos que requiramos...
    def Study(self):
        self.knowlegde+=1

    ### si quiero llamar un método de la clase anterior, debo dejarla explícita
    def callMethod(self):
        age = Person.getAge(self)
        return age

print('\n-----------------')
alice = Student('Alice Smith', 1995)
print(alice)
print(alice.knowlegde)
alice.Study()
print(alice.knowlegde)
print(alice.getAge())   ### Puedo llamar un método que estaba en la clase Padre 
print(alice.callMethod())   ### 