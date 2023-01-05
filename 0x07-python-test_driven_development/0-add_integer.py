#!/usr/bin/python3
"""This is a module with a function that adds 2 integers."""


def add_integer(a, b=98):
    """function that adds 2 integers."""
    if  (type(a) != int) and (type(a) != float):
        raise TypeError("a must be an integer")
    elif (type(b) != int) and (type(b) != float):
        raise TypeError("b must be an integer")
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
        return a + b
    else:
        return a + b