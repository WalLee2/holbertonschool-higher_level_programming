#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    if sentence is not None:
        for i in range(len(sentence)):
            length += 1
            first_char = sentence[0]
        return (length, first_char)
    return (length, None)
