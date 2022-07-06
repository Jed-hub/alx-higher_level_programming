#!usr/bin/python3
"""
Module with append_write function
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a
    text file and returns the number of characters written
    """
    with open(filename, 'a', encoding="utf8") as a_file:
        a_file.write(text)
        num = 0
        for character in text:
            num += 1
        return num
