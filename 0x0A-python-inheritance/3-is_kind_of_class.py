#!/usr/bin/python3
"""
A module that checks if the obj is an instance of the class\
that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,\
    or if the object is an instance of a class that\
    inherited from, the specified class ; otherwise False.
    """
    if type(obj) is not a_class:
        return True
