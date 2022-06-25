#!/usr/bin/python3
"""
    a function that prints a text with 2 new lines\
    after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
     a function that prints a text with 2 new lines\
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for delimiter in ".:?":
        text = (delimiter + "\n\n").join([line.strip(" ") for line in text.split(delimiter)])
    print("{}".format(text), end="")
