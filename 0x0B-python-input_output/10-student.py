#!/usr/bin/python3
"""
    A module that contains the class Student
"""

class Student:
    """
        A class that defines a student by
        first_name, last_name, age.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Retrieves the dictionary representation of Student class\
            if the attr is in attrs retrieve only the name if not all
        """
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
