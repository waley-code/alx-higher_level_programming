#!/usr/bin/python3
def raise_exception():
    raise TypeError("waley-code")
        

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")