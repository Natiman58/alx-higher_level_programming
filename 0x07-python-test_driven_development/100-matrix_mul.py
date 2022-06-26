#!/usr/bin/python3
"""
     A function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    A function that multiples 2 matrices and\
    returns the result
    """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    for x in m_a:
        if not isinstance(x, list):
            raise TypeError("m_a must be a list of lists")
    for y in m_b:
        if not isinstance(y, list):
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for y in row:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) > len(m_a[0]) or len(row) < len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for column in m_b:
        if len(column) > len(m_b[0]) or len(column) < len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    row_a = 0
    for row in m_a[0]:
        row_a += 1
    col_b = 0
    for col in m_b:
        col_b += 1

    if row_a != col_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
