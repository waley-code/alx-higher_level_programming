#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request
from urllib import request, parse
import sys

mail = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')

# Sending a post request
with request.urlopen(sys.argv[1], mail) as rep:
    response_bd = rep.read().decode('utf-8')

print(response_bd)
