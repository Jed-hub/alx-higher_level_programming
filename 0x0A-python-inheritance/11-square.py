#!/usr/bin/python3
"""
The module with the class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
        self.area()

    def __str__(self):
        """Method that return str"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
