#!/usr/bin/python3
import sys


def add_args():
    """This function adds all command line arguments"""
    length = len(sys.argv)
    sum = 0
    for i in range(1, length):
        sum += int(sys.argv[i])
    print(sum)


if __name__ == "__main__":
    add_args()
