#!/usr/bin/python3
import sys


def _args():
    """This function prints the list of command line argument"""
    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:".format(length))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    _args()
