###### TUPLES PACKING
print('>>>>>>>>>>>>>>>>>> TUPLES PACKING <<<<<<<<<<<<<<<<')
julia = ('Julia', 'Roberts', 1967, 'Duplicity', '2009', 'Actress', 'Atlanta, Georgia')
print(julia[4])


## Return value
print('\n--------->>>> Tuples and Return value <<<<<------------')

def cicleFor(n):
    c = 2*n
    a = n**2
    return(c, a)
    #return c, a

print(cicleFor(10))

###### TUPLES UNPACKING
print('\n>>>>>>>>>>>>>>>>>> TUPLES UNPACKING <<<<<<<<<<<<<<<<')

tuple1 = 'Messi', 'Psg', 'Soccer'
print(tuple1)

# assigning
player, team, sport = tuple1
print(player, team, sport)


###### PASSING TUPLE TO A FUNCTION
print('\n>>>>>>>>>>>>>>>>>> PASSING TUPLE TO A FUNCTION <<<<<<<<<<<<<<<<')
def add(x,y):
    return x+y

z = (5,6)
print(z)
print(add(*z))
