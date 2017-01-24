#!/usr/bin/python3
"""
Creating a class named square with a private instance attribute.
"""


class Square:
    """
    Instantiating the variables self and size.
    Raising errors if conditions are not met.
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
