#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for a in range(97, 123):
        if c == a:
            return True
    return False
