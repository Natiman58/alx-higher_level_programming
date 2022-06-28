#!/usr/bin/python3

"""
    A function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    A function that returns the matrix\
    product of 2 matrices using numpy
    """
    return np.matmul(m_a, m_b)
