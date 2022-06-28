#!/usr/bin/python3
"""
    that prevents the user from dynamically creating new instance attributes,\
    except if the new instance attribute is called first_name.
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """Initialize an empty locked class"""
        pass
