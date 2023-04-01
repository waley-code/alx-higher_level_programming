#!/usr/bin/python3
# sends a request to the URL and displays the value of the variable X-Request-Id
import sys
import requests

rep = requests.get(sys.argv[1])
if 'X-Request-Id' in rep.headers:
    print(rep.headers['X-Request-Id'])
