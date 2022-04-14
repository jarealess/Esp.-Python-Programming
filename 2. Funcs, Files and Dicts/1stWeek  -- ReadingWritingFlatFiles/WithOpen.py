# With Open to Read File 

# fname = 'datosclientes.txt'
# with open(fname, 'r') as dc:
# #with open('datosclientes.txt', 'r') as dc:
#     for line in dc:
#         print(line)


fname2='squares2.txt'
with open(fname2, 'w') as dc2:
    for number in range(20):
        dc2.write(f'The square of {number} is: {number**2}\n')