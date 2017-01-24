#!/usr/bin/python3
"""
Creating a class named square with a private instance attribute.
"""


class Square:
    """
    Creating a Square class and instantiating the variables self and size.
    Size is a private variable.
    """
    def __init__(self, size):
        self.__size = size
