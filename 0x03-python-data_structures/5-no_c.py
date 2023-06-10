#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        new_string += x
    return new_string
