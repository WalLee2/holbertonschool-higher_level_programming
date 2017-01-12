#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) < 2):
        if (len(tuple_a) == 1):
            tuple_1 = (tuple_a[0], 0)
        elif (len(tuple_a) == 0):
            tuple_1 = (0, 0)
    else:
        tuple_1 = tuple_a
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_2 = tuple_b[0], 0
        elif len(tuple_b) == 0:
            tuple_2 = (0, 0)
    else:
        tuple_2 = tuple_b
    new = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return (new)
