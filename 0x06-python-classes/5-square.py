#!/usr/bin/python3
""" This module create a class Square with a private instance attribute """


class Square:
    """ The class square that defines a square by size"""
    def __init__(self, size=0):
        """ Initialisation of the attribute size """
        self.size = size

    @property
    def size(self):
        """ Retrieves the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size**2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        for n in range(self.__size):
            if self.__size == 0:
                print()
            else:
                print("#"*self.__size)
