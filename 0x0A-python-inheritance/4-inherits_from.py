#!/usr/bin/python3
"""
    This module contains
    a function that returns True if the object is exactly
    an instance of the specified class
    otherwise False.
"""


def inherits_from(obj, a_class):
    """
        returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class
        otherwise False.
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
