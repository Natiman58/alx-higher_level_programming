#!/usr/bin/python3
"""
    A module that contains a function that returns the dictionary description\
    with simple data structure (list, dictionary, string, integer and boolean)\
    for JSON serialization of an object:
"""


def class_to_json(obj):
    """Returns the dictionary description of a json object"""
    return obj.__dict__
