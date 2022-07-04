#!/usr/bin/python3
"""
    Inheritance
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def print_sorted(self):
        """
            Prints the sorted elements
        """
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
