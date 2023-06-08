#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def calculations():
    """function that performs a number of calculations"""
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    """Program runs only when executed directly"""
    calculations()
