#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a class square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value of size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        overloading __str__ method
        """
        s1 = "[Square] (" + str(self.id) + ") " + str(self.x) + "/"
        s2 = str(self.y) + " - " + str(self.width)
        s = s1 + s2
        return s

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if 'size' in kwargs:
            kwargs['width'] = kwargs['size']
            kwargs['height'] = kwargs['size']
            del kwargs['size']
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)


