#!/usr/bin/env python3
import re
import operator

different_errors = {}
user_entries = {}

with open('syslog.log', 'r') as f:
     logs = f.readlines()
     pattern = r'\: ([A-Z]*) ([a-zA-Z ]*).*\(([a-zA-Z.]*)\)'
     for line in logs:

         try:
            result = re.search(pattern, line.strip())
            code, error, username = result.groups()

            if error not in different_errors:
               different_errors[error]=1
            else:
               different_errors[error]+=1


            if username not in user_entries:
               user_entries[username]={}
               user_entries[username]['INFO'] = 0
               user_entries[username]['ERROR'] = 0

            if code == 'INFO':
               user_entries[username]['INFO']+=1
            elif code == 'ERROR':
               user_entries[username]['ERROR']+=1
         except:
            continue

errors = sorted(different_errors.items(), reverse=True, key=operator.itemgetter(1))
per_user = sorted(user_entries.items(), key=operator.itemgetter(0))

errors.insert(0, ('Error', 'Count'))
##per_user.insert(0, ('Username', 'INFO', 'ERROR'))


with open('error_message.csv', 'w') as error_csv:
     for error, count in errors:
         error_csv.write(error+','+str(count)+'\n')

with open('user_statistics.csv', 'w') as user_csv:
     user_csv.write('Username,'+'INFO,'+'ERROR'+'\n')
     for username, value in per_user:
         user_csv.write(username+','+str(value['INFO'])+','+str(value['ERROR'])+'\n')


