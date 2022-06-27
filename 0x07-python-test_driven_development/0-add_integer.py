#!/usr/bin/python3
"""
This module makes the addition of 2 integers
and raises exceptions when an error occures
It returns the result
"""

def add_integer(a, b=98):
    """ Takes 2  integers a and b as argument
    Returns the addition on the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return(int(a + b))
