#!/usr/bin/python3
"""script that takes your GitHub credentials (username and password)"""
import sys
import requests

if __name__ == "__main__":
    rep = requests.get("https://api.github.com/user",\
            auth=(sys.argv[1], sys.argv[2] ))
    if rep.status_code == 200:
        data = rep.json()
        print(data["id"])

