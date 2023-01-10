#!/usr/bin/python3
"""
    contains a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
"""
import json


def load_from_json_file(filename):
    """
    reads a text file to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
