#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = [[i ** 2 for i in row] for row in matrix]
    return my_matrix
