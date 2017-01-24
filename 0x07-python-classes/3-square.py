#!/usr/bin/python3

"""
Creating a class named square with a private instance attribute.
Defining another function within the class that finds the square of size.
"""


class Square:

    """
    Instatiating a method and checks if size is an integer or greater than 0
    Creating a method that returns the square of size.
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
