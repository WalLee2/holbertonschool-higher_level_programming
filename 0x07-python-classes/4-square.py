#!/usr/bin/python3
"""
Creating a class named square with a private instance attribute.
Defining another function within the class that finds the square of size.
"""


class Square:
    """
    Instantiating a size variable and making it private.
    Raising errors if size is less than 0
    Raising errors if size is not an int
    Using setter and getter
    Creating a method that finds the square of a number.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
