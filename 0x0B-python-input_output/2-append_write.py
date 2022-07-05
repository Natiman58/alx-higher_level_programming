#!/usr/bin/python3

"""
    A module that holds the append_write function\
    at the end of a txt file (UTF8) and\
    returns the nmber of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of file"""
    with open(filename, "a", encoding="utf8") as f:
        return f.write(text)
