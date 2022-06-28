#!/usr/bin/python3
"""
This module contain a function
that prints a square
with the character #
"""


def print_square(size):
    """ This function prints a square
    with the given agrgument as size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for n in range(size):
        for n in range(size):
            print("#", end="")
        print()
