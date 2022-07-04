#!/usr/bin/python3
"""
A module that creates a square by inheritance.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class called square that passes size 2X hence width\
    and height are same for a square
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method to calculate area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string format of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
