#!/usr/bin/python3
""" Python script that takes 2 arguments in order
    to solve this challenge.
"""
from sys import argv
import requests

if __name__ == "__main__":
    rep = requests.get(f"https://developer.github.com/v3/repos/{argv[2]}/{argv[1]}/commits/")
    if rep.status_code == 200:
        com_msg = rep.json()
        for com in com_msg[:10]:
            sha = com.get("sha")
            name = com['commit']['author']['name']
            print(f"{sha}: {name}")
    else:
        print("Error while trying to retrieve commits. Error: {}".format(rep.status_code))

