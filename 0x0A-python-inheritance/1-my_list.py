#!/usr/bin/python3

"""
Define a class MyList
Inherits properties from list
"""


class MyList(list):
    """
    MyList class with list as parent
    """
    def __init__(self):
        """
        initialize properties
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list in ascending order
        """
        print(sorted(self))
