#!/usr/bin/python3
"""
    A module containing the class 'Base'\
    This class will be the “base” of all\
    other classes in this project.\
    The goal of it is to manage id attribute\
    in all your future classes and to avoid\
    duplicating the same code (by extension, same bugs).
"""


class Base:
    """
        A base class with private class attribute '__nb_objects'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize the attributes.
            arg:
                id - argument value of id
                'self.id' - public instance attribute id
        """
        if id is not None and id is int:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
