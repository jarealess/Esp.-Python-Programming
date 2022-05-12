# https://realpython.com/python-csv/
# https://docs.python.org/3/library/csv.html

#####---------------------- Reading CSV 
import csv
import os

os.chdir('2Week')

f = open('NoHeaderCsv.txt')
csv_f = csv.reader(f)
for row in csv_f:
    print(row)

f.close()


#####---------------------- Generaating CSV (WRITEROWS)
hosts = [['workstation.local','192.168.25'], ['webserser.cloud', '10.2.5']]
with open('hosts.csv', 'w') as host_csv:
    writer = csv.writer(host_csv)
    writer.writerows(hosts)


#### ------------------------ DICTREADER
with open('hosts.csv') as hosts1:
    reader = csv.DictReader(hosts1)
    for row in reader:
        print(row)


###-------------------------- DICTWRITER
### Pasamos una lista de diccionarios y los convierte a CSV
users = [{'name':'Sol Mansi', 'username':'solm', 'deparment':'IT Architecture'},
        {'name':'Lio Nelson', 'username':'lion', 'deparment':'Experience Reseach'},
        {'name':'Charlie Grey', 'username':'greyc', 'deparment':'Development'}]

Dictkeys = list(users[0].keys())
with open('ByDeparment.csv', 'w') as by_deparment:
    writer = csv.DictWriter(by_deparment, fieldnames=Dictkeys)
    writer.writeheader()
    writer.writerows(users)