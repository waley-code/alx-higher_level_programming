#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
    content = rep.read()
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {content.decode('utf-8')}")
