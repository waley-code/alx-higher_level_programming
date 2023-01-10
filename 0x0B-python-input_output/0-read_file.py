#!/usr/bin/python3
"""This module creates  a function that reads a text
    file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    reads a text file to stdout
    """
    with open(filename, 'r', encoding="utf-8") as rf:
        readFile = rf.read()
        print(readFile)