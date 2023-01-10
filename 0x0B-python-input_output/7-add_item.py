#!/usr/bin/python3
"""Module comntains list arg"""
import json
import sys
import os.path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
x = []

if os.path.exists(filename):
    x = load_from_json_file(filename)
for i in  argv[1:]:
    x.append(i)

save_to_json_file( x, filename)
