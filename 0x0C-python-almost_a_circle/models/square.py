#!/usr/bin/python3
"""
    A module containing a square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        A square class that inherits from the rectangle class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initialize the attributes by using the attributes of the\
            superclass; Rectangle\
            Call the super class with id, x, y, width and height\
            this super call will use the logic of the __init__ of the Rectangle class.\
            The width and height must be assigned to the value of size
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square class."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Retrieves the size attribute."""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the value for size."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value


