#!/usr/bin/python3
""" This module create a class Square with a private instance attribute """


class Square:
    """ The class square that defines a square by size"""
    def __init__(self, size=0):
        """ Initialisation of the attribute size """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except (TypeError, NameError):
            raise TypeError("size must be an integer")
