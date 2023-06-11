#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        return len(sentence), None
    for letter in sentence:
        if letter == sentence[0]:
            return len(sentence), letter
