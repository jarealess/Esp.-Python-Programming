######################3 UNIT TEST ##########################33
## La forma más común para desarrollar pruebas automáticas

## https://docs.python.org/3/library/unittest.html#basic-example


import re 

def rearrange_name(name):
     pattern = '^([\w .]*), ([\w .]*)$'
     result = re.search(pattern, name)
     
     if result is None:
         return name
     return f'{result[2]} {result[1]}'



