## WRITING
UserDirectory = [['Janick Reales', 27, 'Quibdó'], 
                 ['Samantha Arboleda', 26, 'Niquía'],
                 ['Naruto Uzumaki',16, 'Konoha']]

OutputFile = open('UserDirectory.csv', 'w')
#header row
header = 'Name,Age,Location'
OutputFile.write(header+'\n')

# Outputs
for row in UserDirectory:
   # row_string='{},{},{}\n'.format(row[0], row[1], row[2])
    row_string = ','.join([row[0], str(row[1]), row[2]])
    OutputFile.write(row_string+'\n')

OutputFile.close()


