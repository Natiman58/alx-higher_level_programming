#!/usr/bin/python3
"""
    A module containg the function 'pascal_triangle'
"""


def pascal_triangle(n):
    """
        A function that returns a list of integers representing
        pascal's triangle of n
    """
    if n <= 0:
        return []
    lis_t = []
    for i in range(n):
        if i == 0:
            lis_t.append([1])
            continue
        if i == 1:
            lis_t.append([1, 1])
            continue
        row = []
        for item in range(i + 1):
            row.append(item)
        for item in range(1, i):
            row[0] = 1
            row[i] = 1
            row[item] = lis_t[i - 1][item] + lis_t[i - 1][item - 1]
        lis_t.append(row)
    return lis_t
