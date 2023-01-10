#!/usr/bin/python3
"""
    contains a function that  appends a string at the end of a text file
    and returns the number of characters written:
"""


def append_write(filename="", text=""):
    """
     appends a string at the end of a text file
    """
    with open(filename, 'a', encoding="utf-8") as rf:
        return rf.write(text)