#!/usr/bin/python3
"""
    A module that holds an inverted class\
    that inherits from int super class\
    and returns the opposite;\
    equal is interpreted as not equal\
    and vice versa.
"""


class MyInt(int):
    """A class that inverts results."""
    def __eq__(self, value):
        """A magic method that is called by default\
        when we use '==' sign and returns the opposite"""
        return super().__ne__(value)

    def __ne__(self, value):
        """
        A magic method that is called by default\
        when we use '!=' sign and returns the opposite.
        """
        return super().__eq__(value)
