#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return None
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    sum_a = tuple_a[0] + tuple_b[0]
    sum_b = tuple_a[1] + tuple_b[1]
    new_tuple = (sum_a, sum_b)
    return new_tuple
