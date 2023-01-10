#!/usr/bin/python3
"""
    contains a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    reads a text file to stdout
    """
    with open(filename, 'w', encoding="utf-8") as rf:
        return rf.write(text)