#!/usr/bin/python3
def multiple_returns(sentence):
    """A function that returns a tuple with the\
            length of a string and its first character"""
    if sentence == 0:
        return None
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tuple = (length, first_char)
        return new_tuple
