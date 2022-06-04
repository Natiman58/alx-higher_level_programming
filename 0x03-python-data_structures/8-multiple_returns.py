#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        new_tuple[0] = "None"
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tuple = (length, first_char)
        return new_tuple
