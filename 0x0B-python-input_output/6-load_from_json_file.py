#!/usr/bin/python3
"""
    A module that contains a function
    that creates an object from a "JSON file"
"""

import json


def load_from_json_file(filename):
    """Returns the object representation of the json file 'filename'"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
