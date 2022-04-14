def f(x):
    return x-1

print(f(3))

################ with lambda ###################
### El return es implícito
print('\n')
lf = lambda x: x-1
print(lf(3))

def checkingIfIn(str1, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
        if direction:
            if str1 in d:
                return True
            else:
                False
        else:
            if str1 not in d:
                return True
            else:
                False

checkingIfIn()