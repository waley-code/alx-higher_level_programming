#!/usr/bin/python3
# script that takes in a letter and sends a POST request
import sys
import requests

if len(sys.argv) == 2:
    que = sys.argv[1]
else:
    que = ""

rep = requests.post('http://0.0.0.0:5000/search_user', data={'q': que})
try:
    jd = rep.json()
    if jd:
        print(f"[{jd.id}] {jd.name}")
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
