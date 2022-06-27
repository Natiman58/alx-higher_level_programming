#!/usr/bin/python3
"""
    A module that defines a rectangle\
     by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
    A class with attributes.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the attributes.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the object."""
        return self.__width

    @width.setter
    def width(self, value):
        """
            Sets the width of a Rectangle instance to a value.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the object.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height to a value.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value



