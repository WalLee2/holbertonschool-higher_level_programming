#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None
    if sentence is not None:
        for i in sentence:
            length += 1
            first_char = sentence[0]
    return (length, first_char)
