#!/usr/bin/python3
from add_0 import add

def simple_func():
    """Function that adds two numbers"""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    """code runs only when executed directly"""
    simple_func()
