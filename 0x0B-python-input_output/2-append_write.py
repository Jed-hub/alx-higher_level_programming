#!usr/bin/python3
"""
Module with append_write function
"""


def append_write(filename="", text=""):
    """
    Description: Function that writes a string to a text file.
    Args:
        filename: file to write.
        text: text to add to the filename.
    """
    with open(filename, 'a', encoding="utf8") as a_file:
        a_file.write(text)
        num = 0
        for character in text:
            num += 1
        return num
