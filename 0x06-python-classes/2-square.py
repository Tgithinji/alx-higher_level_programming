#!/usr/bin/python3

"""a class that defines a square"""


class Square:
    """a class Square the defines a square by
    a private instance of size"""
    def __init__(self, size=0):
        """Initialize data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
