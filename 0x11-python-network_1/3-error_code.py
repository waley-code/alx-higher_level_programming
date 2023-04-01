#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the body"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen() as rep:
            content = response.read().encode('utf-8')
        print(f"Response body: {content}")
    except error.HTTPError as fp:
        print("Error code:", fp.code)
