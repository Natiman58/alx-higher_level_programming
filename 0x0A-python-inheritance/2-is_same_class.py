#!/usr/bin/python3
"""
A module that checks if the obj is\
is in the same class.
"""


def is_same_class(obj, a_class):
    """a function that returns True\
    if the object is exactly an instance of the specified class;\
    otherwise False."""
    if type(obj) is a_class:
        return True
    else:
        return False
