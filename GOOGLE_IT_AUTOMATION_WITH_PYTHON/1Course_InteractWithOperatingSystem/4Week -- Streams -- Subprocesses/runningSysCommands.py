#### RUNNING SYSTEM COMMANDS IN PYTHON

import subprocess


### linux commands
subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(['ls', 'thisFileDoesNotExist'])
print(result.returncode)



### OBTAINING THE OUTPUT OF A SYSTEM COMMAND
result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.stdout)
print(result.stdout.decode().split())