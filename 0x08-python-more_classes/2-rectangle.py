#!/usr/bin/python3

"""
This class defines a rectangle
"""


class Rectangle:
    """
    This class includes private instance atrributes
    width and height
    public methods to find area and perimeter of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes an instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieves the witdh
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the value of height
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
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
