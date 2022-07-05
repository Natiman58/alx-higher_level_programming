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
            Retrieves the dictionary representation of Student class.
            if the attr is in attrs retrieve only the name if not all
        """
        if type(attrs) != list:
            return self.__dict__
        else:
            temp = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    temp[i] = self.__dict__[i]
            return temp
