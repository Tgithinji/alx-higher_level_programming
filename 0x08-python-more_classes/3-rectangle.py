#!/usr/bin/python3

"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Difines a rectangle class with attributes
    """
    def __init__(self, width=0, height=0):
        """
        initializes an instance with attributes
        width(int)
        height(int)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter of rectangle
        """
        if self.__width == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a rectangle with the character #
        """
        rect_string = ""
        if self.__width == 0 or self.__height == 0:
            return rect_string
        for i in range(self.__height):
            for x in range(self.__width):
                rect_string += "#"
            if i == (self.__height - 1):
                break
            else:
                rect_string += "\n"
        return rect_string
