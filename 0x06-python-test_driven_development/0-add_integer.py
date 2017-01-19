#!/usr/bin/python3
"""
Adding two numbers and raising errors if values are not floats or ints.
"""


def add_integer(a, b):
    """
    Raise TypeError if a or b is a bool.
    Raise TypeError for every case that is not either an integer or a float.
    If number is a float convert it to an int.
    Add two numbers together.
    """

    if ((isinstance(a, (int, float))) and isinstance(b, (int, float))):
        a = int(a)
        b = int(b)
        return a + b
    if (isinstance(a, (int, float)) is False):
        raise TypeError("a must be an integer")
    if (isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
