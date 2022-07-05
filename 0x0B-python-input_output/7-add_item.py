#!/usr/bin/python3
"""
    A script that adds all arguments to a python list\
    and save them to a json file.
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_jason_file = __import__('5-save_to_json_file').save_to_json_file

try:
    l_file = load_from_json_file("add_item.json")
except FileNotFoundError:
    l_file = []


for i in range(1, len(sys.argv)):
    l_file.append(sys.argv[i])
save_to_jason_file(l_file, "add_item.json")
