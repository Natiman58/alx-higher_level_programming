#!/usr/bin/python3
"""
    A module that adds an attribute to an obj if possible.
"""


def add_attribute(oj_name, at_name, at_value):
    """
    a method that adds an attribute to an obj.\
    'oj_name' - object name\
    'at_name' - attribute name\
    'at_value' - attribute value we want to set
    """

    if not hasattr(oj_name, '__slots__') and not hasattr(oj_name, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(oj_name, '__slots__') and not hasattr(oj_name, at_name):
        raise TypeError("can't add new attribute")
    setattr(oj_name, at_name, at_value)
