#!/usr/bin/python3
""" This module create a class Square with a private instance attribute """


class Square:
    """ The class square that defines a square by size"""
    def __init__(self, size=0, position=(0, 0)):
        """ Initialisation of the attribute size and position """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrieves the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Returns the current square area """
        return self.__size**2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
