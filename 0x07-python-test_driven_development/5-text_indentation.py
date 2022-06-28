#!/usr/bin/python3
"""
THis module has one function
for the text indentation
"""


def text_indentation(text):
    """
    This function takes a text like argument
    and prints it with 2 new lines after each
    of the characters . ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for c in text:
        if flag == 0:
            if c == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                flag = 0
            else:
                print(c, end="")
