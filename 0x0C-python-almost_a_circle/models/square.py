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
        self.size = size
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

    @property
    def size(self):
        """
        the getter
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        the setter
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        the update method assigns an argument
        to each attribute
        """
        arg_list = []
        arg_dict = {}

        if kwargs is not None:
            for key, value in kwargs.items():
                arg_dict[key] = value
            if 'id' in arg_dict:
                self.id = arg_dict['id']
            if 'size' in arg_dict:
                self.width = arg_dict['size']
            if 'x' in arg_dict:
                self.x = arg_dict['x']
            if 'y' in arg_dict:
                self.y = arg_dict['y']

        for arg in args:
            arg_list.append(arg)
        if len(arg_list) >= 1:
            self.id = arg_list[0]
        if len(arg_list) >= 2:
            self.width = arg_list[1]
        if len(arg_list) >= 3:
            self.x = arg_list[2]
        if len(arg_list) >= 4:
            self.y = arg_list[3]

    def to_dictionary(self):
        """
        the method to_dictionary returns
        the dictionary representation of a rectangle
        """
        r_dict = {}
        if self.id:
            r_dict['id'] = self.id
        if self.x:
            r_dict['x'] = self.x
        if self.size:
            r_dict['size'] = self.size
        if self.y:
            r_dict['y'] = self.y

        return r_dict
