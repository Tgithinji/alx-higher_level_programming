#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_v = float('-inf')
    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            key = k
    return key
