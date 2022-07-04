#!/usr/bin/python3
"""
    A function that returns list of available attributes
    and methods of an object.
"""


def lookup(obj):
    """ Returns all the lists of attributes """

    return dir(obj)
