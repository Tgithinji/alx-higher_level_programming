#!/usr/bin/python3

"""
This module defines a class My_Int
"""


class MyInt(int):
    """
    MyInt class that inherits from int
    """
    def __eq__(self, other):
        """
        Inverts the == operator to !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator to ==
        """
        return super().__eq__(other)
