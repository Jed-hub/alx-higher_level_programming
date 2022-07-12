#!/usr/bin/python3
"""
The module square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization
        """
        #self.size = size
        width = size
        height = size
        super().__init__(width, height, x, y, id=None)
        self.width = size
        self.height = size

    def __str__(self):
        """
        str method returns a string
        """
        return ("[Square] (" + str(self.id) + ") "
                + str(self.x) + "/" + str(self.y)
                + " - " + str(self.width))
