#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_avg = 0
    sum_denom = 0
    for tple in my_list:
        mul = 1
        for x in tple:
            mul *= x
        sum_avg += mul
        sum_denom += x
    return sum_avg / sum_denom
