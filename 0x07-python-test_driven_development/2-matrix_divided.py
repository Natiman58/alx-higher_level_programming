#!/usr/bin/python3
"""
    A function that divides all elements of a matrix
    and returns a new matrix containing each division result

"""


def matrix_divided(matrix, div):
    """
    A function that divides each element\
     of a matrix by a given value(div)
    """
    new_list = []

    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        inner_list = []
        for items in lists:
            if type(items) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            else:
                inner_list.append(round(items / div, 2))
        new_list.append(inner_list)
    return new_list
