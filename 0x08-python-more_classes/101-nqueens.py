#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""


def isSafe(q_pos, q_num):
    """ Method that determines if the queens will or won't kill each other
    Args:
        q_pos: array that has the queens positions
        q_num: queen number
    Returns:
        True: when queens can't kill each other
        False: when some queens can kill each other
    """

    for i in range(q_num):

        if q_pos[i] == q_pos[q_num]:
            return False

        if abs(q_pos[i] - q_pos[q_num]) == abs(i - q_num):
            return False

    return True


def print_result(q_pos, q_num):
    """ Method that prints the list with the Queens positions
    Args:
        q_pos: array that has the queens positions
        q_num: queen number
    """
    res = []
    for i in range(q_num):
        res.append([i, q_pos[i]])

    print(res)


def Queen(q_pos, q_num):
    """ Recursive function that executes the Backtracking algorithm
    Args:
        q_pos: array that has the queens positions
        q_num: queen number
    """
    if q_num is len(q_pos):
        print_result(q_pos, q_num)
        return

    q_pos[q_num] = -1

    while q_pos[q_num] < len(q_pos) - 1:

        q_pos[q_num] += 1

        if isSafe(q_pos, q_num) is True:

            if q_num is not len(q_pos):
                Queen(q_pos, q_num + 1)


def solveNQueen(size):
    """ Function that invokes the Backtracking algorithm
    Args:
        size: size of the chessboard
    """

    q_pos = [-1 for i in range(size)]
    Queen(q_pos, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)
