#!/usr/bin/python3
"""
    A module containing a student class.
"""


class Student:
    """
        A class that defines a student by
        first_name, last_name, age
    """
    def __int__(self, first_name, last_name, age):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of a student class."""
        return self.__dict__
