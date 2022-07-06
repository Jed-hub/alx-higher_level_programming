#!/usr/bin/python3
"""
My class module
"""


def class_to_json(obj):
    """
    Return the dictionary description
    with the simple data structure
    """
    return obj.__dict__
