#!/usr/bin/python3
"""
     a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, name, title):
    """Sets object attribute"""
    if type(obj) is str:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, title)