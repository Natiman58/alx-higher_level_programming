#!/usr/bin/python3
"""
    A module that contains
    'from_json_string(my_str)' function.
"""

import json


def from_json_string(my_str):
    """Returns an obj representation of the json string; my_str"""
    return json.loads(my_str)
