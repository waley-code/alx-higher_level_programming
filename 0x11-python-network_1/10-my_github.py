#!/usr/bin/python3
# script that takes your GitHub credentials (username and password)
import sys
import requests

rep = requests.get("https://api.github.com/waley-code", auth=(sys.argv[1], sys.argv[2] ))
if rep.status_code == 200:
    data = rep.json()
    print("User ID:", data["id"])
else:
    print("Error:", rep.status_code)
