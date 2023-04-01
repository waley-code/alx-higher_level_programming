#!/usr/bin/python3
"""script that takes your GitHub credentials
    (username and password)
"""
from requests.auth import HTTPBasicAuth
import sys
import requests

if __name__ == "__main__":
    rep = requests.get("https://api.github.com/user",
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    data = rep.json()
    print(data["id"])
