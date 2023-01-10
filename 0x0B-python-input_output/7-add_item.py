#!/usr/bin/python3
"""Module comntains list arg"""
import json
import sys
import os.path
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

x = []

if os.path.exists("add_item.json"):
    x = load_from_json_file("add_item.json")
for i in  argv[1:]:
    x.append(i)

save_to_json_file( x, "add_item.json")
