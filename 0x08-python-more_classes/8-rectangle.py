#!/usr/bin/python3

"""
Defines a Rectangle class
"""


class Rectangle:
    """
    A Rectangle class with both public class attributes
    and private instance attributes
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize an instance of Rectangle
        width(int)
        height(int)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        deletes an instance of rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Retrieve the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        """
        calculate perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        creates a rectangle with # character
        """
        rect = ""
        for i in range(self.__height):
            for x in range(self.__width):
                rect += str(self.print_symbol)
            if i == self.__height - 1:
                break
            else:
                rect += "\n"
        return rect

    def __repr__(self):
        """
        Returns a string reprecentation
        """
        s = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return s

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """
        static method to find the bigger rectactangle
        """
        if not isinstance(rect1, Rectangle):
            raise TypeError("rect1 must be an instance of rectangle")
        if not isinstance(rect2, Rectangle):
            raise TypeError("rect2 must be an instance of Rectangle")
        if rect1.area() > rect2.area():
            return rect1
        elif rect1.area() == rect2.area():
            return rect1
        else:
            return rect2
