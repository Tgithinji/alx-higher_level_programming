#!/usr/bin/python3

"""a class that defines a square"""


class Square:
    """a class square with a 
    private instance of size and
    a public instance method that returns area"""
    def __init__(self, size=0):
        """Initialize data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must not be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area by size"""
        return self.__size * self.__size
