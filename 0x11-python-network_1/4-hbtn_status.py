#!/usr/bin/python3
# n script that fetches https://alx-intranet.hbtn.io/status
import requests

rep = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print(f"\t- type {type(rep.text)}")
print(f"\t- content: {rep.text}")
