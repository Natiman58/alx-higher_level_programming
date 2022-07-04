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
    set_t = {str}

    if type(oj_name) in set_t:
        raise TypeError("Can't add new attribute")
    else:
        oj_name.__setattr__(at_name, at_value)
