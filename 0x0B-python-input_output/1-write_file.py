#!/usr/bin/python3
"""
    A module that holds the 'write_file' function.
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)\
    and returns the number of characters written,\
    filename: name of the file to be written in\
    text: the texts to add to the text file.\
    """
    with open(filename, 'w',  encoding="utf-8") as f:
        return f.write(text)
