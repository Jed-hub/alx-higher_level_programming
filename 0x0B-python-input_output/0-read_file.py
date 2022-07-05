#!/usr/bin/python3
"""
Module with the function read_file
"""


def read_file(filename=""):
    """
    This function reads a text file
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
