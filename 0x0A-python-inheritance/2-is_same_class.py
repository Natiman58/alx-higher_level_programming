#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Returns true if the obj is in the same class"""
    if type(obj) is a_class:
        return True
    else:
        return False
