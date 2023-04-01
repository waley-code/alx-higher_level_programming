#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
import sys
import requests

if __name__ == "__main__":
    rep = requests.get(sys.argv[1])
    if rep.status_code >= 400:
        print(f"Error code: {rep.status_code}")
    else:
        print(rep.content.decode('utf-8'))
