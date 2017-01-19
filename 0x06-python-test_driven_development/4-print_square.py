#!/usr/bin/python3
"""
Printing out a square using the "#" symbol.
"""


def print_square(size):
    """
    Raising TypeError if the size is not an int or a float or
    if size is a True or False value.
    Raising TypeError if the size is less than 0
    Raising TypeError if size is a float and less than 0
    """
    if not isinstance(size, (int, float)) and isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(0, int(size)):
        print("#" * int(size))
