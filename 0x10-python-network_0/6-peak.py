#!/usr/bin/python3
"""Module with the function find_peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    li = list_of_integers
    length = len(li)
    if length == 0:
        return
    m = length // 2
    if (m == length - 1 or li[m] >= li[m + 1])\
            and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != length - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
