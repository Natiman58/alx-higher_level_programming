#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = "None"
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tuple = (length, first_char)
    return new_tuple
