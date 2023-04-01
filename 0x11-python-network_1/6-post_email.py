#!/usr/bin/python3
"""script that takes in a URL and an email address,
    sends a POST request to the passed UR
"""
import sys
import requests

if __name__ == "__main__":
    rep = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(rep.text)
