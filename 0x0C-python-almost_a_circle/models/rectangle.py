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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Heigth getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Height setter
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x=0):
        """
        x setter
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y=0):
        """
        y setter
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the rectangle instance
        with the character #
        """
        if self.y:
            for n in range(self.y):
                print()
        for h in range(self.height):
            if self.x:
                for n in range(self.x):
                    print(end=" ")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        str method that returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] (" + str(self.id) + ") "
                + str(self.x) + "/" + str(self.y) + " - "
                + str(self.width) + "/" + str(self.height))
