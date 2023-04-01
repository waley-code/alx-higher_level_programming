#!/usr/bin/python3
"""Python script that fetches header from https://alx-intranet.hbtn.io/status"""
from urllib import request
import sys

if __name__ == "__main__":
    # Open a request and receiving response
    with request.urlopen(sys.argv[1]) as rep:
        # getting X-Request-Id value from header
        req_id = rep.getheader('X-Request-Id')

    # Outpuy the value to screen
    print(req_id)
