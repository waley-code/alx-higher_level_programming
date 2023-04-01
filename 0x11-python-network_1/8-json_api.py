#!/usr/bin/python3
"""script that takes in a letter and sends a POST request"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 1:
        que = sys.argv[1]
    if len(sys.argv) == 1:
        que = ""

    rep = requests.post('http://0.0.0.0:5000/search_user', {"q": que})
    try:
        jd = rep.json()
        if jd != {}:
            print(f"[{jd.get('id')}] {jd.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
