#!/usr/bin/python3
"""
    A module that creates a rectangle by inheritance.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """A magic method that returns string format of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
