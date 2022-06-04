#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        return None
    else:
        length = len(sentence)
        first_char = sentence[0]
        new_tuple = (length, first_char)
        return new_tuple
