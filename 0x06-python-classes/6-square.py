#!/usr/bin/python3

""" A class that defines a square"""


class Square:
    """class defining a square"""
    def __init__(self, size=0, position):
        """Initialize data"""
        self.__size = size
        self.position = position

    @property
    def position(self):
        """
        retrieve position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets position to a value
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] > 0 and value[1] > 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """calculate sqare area"""
        return self.__size * self.__size

    def my_print(self):
        """
        print a square with the characyter #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
