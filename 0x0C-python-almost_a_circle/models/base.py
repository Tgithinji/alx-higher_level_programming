#!/usr/bin/python3
"""
This is rhe base module
"""


class Base():
    """
    This creates instances of class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initilizes instances of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
