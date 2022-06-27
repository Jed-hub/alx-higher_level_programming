#!/usr/bin/python3
""" 
This module prints the string
My name is <first_name> <last_name>
"""

def say_my_name(first_name, last_name=""):
    """ The function takes 2 strings as arguments
    the fist name and the last name and prints them
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {0} {1}".format(first_name, last_name))
