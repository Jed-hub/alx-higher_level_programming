#!/usr/bin/python3
"""
Second module
"""


from models.base import Base

class Rectangle(Base):
    """
    Class Rectangle that inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width getter
        """
        return self.width
    @width.setter
    def width(self, width):
        """
        width setter
        """
        self.width = width
    @property
    def height(self):
        """
        Heigth getter
        """
        return self.height
    @height.setter
    def height(self, height):
        """
        Height setter
        """
        self.height = height
    @property
    def x(self):
        """
        x getter
        """
        return self.x
    @x.setter
    def x(self, x=0):
        """
        x setter
        """
        self.x = x
    @property
    def y(self):
        """
        y getter
        """
        return self.y
    @y.setter
    def y(self, y=0):
        """
        y setter
        """
        self.y = y
