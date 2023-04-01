#!/usr/bin/python3
"""script that takes in a URL, sends a request to
    the URL and displays the body
"""

from urllib import request, error
import sys
from urllib.request import Request

if __name__ == "__main__":
    try:
        with request.urlopen(Request(sys.argv[1])) as rep:
            content = rep.read().decode("ascii")
        print(f"Response body: {content}")
    except error.HTTPError as fp:
        print(f"Error code: {fp.code}")
