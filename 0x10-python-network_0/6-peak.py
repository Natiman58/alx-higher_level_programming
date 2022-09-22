#!/usr/bin/python3
"""
    A module containg the peak function
"""

def find_peak(list_of_integers):
    """
        returns the peak in a list of unsorted array
    """
    if list_of_integers is None or list_of_integers == []:
        return None

    lis_t = list_of_integers
    list_len = len(lis_t)

    mid = list_len // 2
    if (mid == list_len - 1 or lis_t[mid + 1]) and (mid == 0 or lis_t[mid] >= lis_t[mid - 1]):
        return lis_t[mid]
    if (mid != list_len - 1 or lis_t[mid + 1] > lis_t[mid]):
        return find_peak(lis_t[mid + 1:])
    return find_peak(li[:m])
