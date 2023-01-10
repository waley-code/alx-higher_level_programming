#!/usr/bin/python3
"""
    contains a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    reads a text file to stdout
    """
    with open(filename, 'w', encoding="utf-8") as rf:
        json.dump(my_obj, rf)