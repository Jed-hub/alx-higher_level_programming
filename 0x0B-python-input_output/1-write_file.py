#!usr/bin/python3
"""
Module with write_file function
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text
    file and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf8") as a_file:
        return a_file.write(text)
