#!/usr/bin/python3
"""
A module containing a class called BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods"""
    def area(self):
        """Raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A method to validate the value entered as proper"""
        """Validates if a name has the proper value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
