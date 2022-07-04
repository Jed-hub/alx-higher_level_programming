#!/usr/bin/python3
"""
The module with the function
is_same_class
"""

def is_same_class(obj, a_class):
    """
    The function returns True
    of the object is exatly an instance
    of the specified class
    otherwise false
    """
    if type(obj) == a_class:
        return True
    else:
        return False
