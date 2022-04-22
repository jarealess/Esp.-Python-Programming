items = ['a','b']

try:
    print('a')
    third = items[2]    #### Ejecuta hasta donde encuentre el error / se salta y ejecuta lo que haya en except
    print('b')
except:
    print('Algo salió mal')
    third = False


#---------- Se puede poner más de un Except, de acuerdo con el tipo de error a manejar

try:
    ##myvar = a
    x = 10/0
    third = items[2]
    print('a')
except ZeroDivisionError:
    print("You can't divide by zero")
except IndexError:
    print("Index out of bounds")
except NameError:
    print("Unknown Variable")
except Exception:  ## Este maneja varios tipos de errores
    print("Something else went wrong")
