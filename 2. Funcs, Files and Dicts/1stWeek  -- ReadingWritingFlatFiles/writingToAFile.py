## writing
file_obj = open('squares.txt', 'w')

for number in range(13):
    square = number*number

    file_obj.write(str(square)+'\n')
    print(square)

file_obj.close()




