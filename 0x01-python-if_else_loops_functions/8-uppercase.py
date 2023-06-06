#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for a in str:
        c = ord(a)
        if c >= 97 and c < 123:
            c = c - 32
            new_str += chr(c)
        else:
            new_str += a
    print("{}".format(new_str))
