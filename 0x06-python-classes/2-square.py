#!/usr/bin/python3
""" This module create a class Square with a private instance attribute """


class Square:
    """ The class square that defines a square by size"""
    def __init__(self, size=0):
        """ Initialisation of the attribute size """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
