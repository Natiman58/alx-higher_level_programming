#!/usr/bin/python3
"""
    A module that defines a rectangle\
     by: (based on 5-rectangle.py)
"""


class Rectangle:
    """
    A class with attributes:
        self.width:  private class attribute.
        self.height:  private class attribute.
        number_of_instances: public class attribute.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize the fields.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
            Returns an informal and nicely printable string representation\
            of the object rectangle, filled with the '#' character.
        """
        rect_str = ''
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += '#'
            rect_str += '\n'
        return rect_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle\
        to be able to recreate a new instance by using eval()\
        of the return value
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints the message Bye rectangle...\
        when an instance of Rectangle is deleted.
         """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """A public instance method to calculate\
        area of the object"""
        return self.__width * self.__height

    def perimeter(self):
        """A public instance method to calculate the\
        perimeter of the object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)
