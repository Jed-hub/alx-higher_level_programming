#!/usr/bin/python3
""" This module create a class Square with a private instance attribute """


class Square:
    """ The class square that defines a square by size"""
    def __init__(self, size):
        """ Initialisation of the attribute size """
        self.__size = size
