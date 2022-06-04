#!/usr/bin/python3
def multiple_returns(sentence):
    """Write a function that returns a tuple with\
             the length of a string and its first character."""
    if len(sentence) == 0:
        new_tuple = ()
        new_tuple = 1, "None"
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tuple = (length, first_char)
        return new_tuple
