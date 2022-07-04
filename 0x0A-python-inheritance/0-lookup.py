#!/usr/bin/python3
"""
    A module that holds a class which\
    returns list of available attributes
    and methods of an object.
"""


def lookup(obj):
    """ Returns all the lists of attributes """

    return dir(obj)
