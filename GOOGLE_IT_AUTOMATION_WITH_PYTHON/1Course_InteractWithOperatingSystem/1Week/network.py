#!/usr/bin/env python3
#https://realpython.com/python-requests/#:~:text=The%20first%20bit%20of%20information,looking%20for%20was%20not%20found.

import requests
import socket

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def check_connectivity():
    response = requests.get("http://www.google.com")
    status_code = response.status_code  ## si es 200 indica que la conexión fue exitosa
    return status_code == 200


# if response.status_code == 200:
#     print('Success!')
# elif response.status_code == 404:
#     print('Not Found.')