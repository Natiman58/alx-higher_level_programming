#!/usr/bin/python3
"""
    A module that contains the 'read_file' function
"""


def read_file(filename=""):
    """A function that reads a text file(UTF8) and prints it to stdout"""
    with open(filename) as f:
        read_data = f.read()
        print(read_data)
