# Reading CSV
fileObj = open('headerCsv.txt', 'r')
lines = fileObj.readlines()
for line in lines:
    print(line.strip())

print('------------------------------')
header=lines[0].strip().split(',')
print(header)
for row in lines[1:]:
    vals=row.strip().split(',')
    print(f'{vals[0]}: {vals[1]} - {vals[2]}, {vals[3]}')
