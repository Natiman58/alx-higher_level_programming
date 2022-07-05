#!/usr/bin/python3
"""
    A module that contains the function\
    that returns the JSON representation of an object(string)
"""
import json


def to_json_string(my_obj):
    """Returns the JSON formatted string representation of my_obj"""
    return json.dumps(my_obj)
