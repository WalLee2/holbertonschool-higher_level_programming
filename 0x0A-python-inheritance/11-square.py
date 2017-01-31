#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
A class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    Class Square inheriting from Rectangle. Returning a string and returning the result
    of size * size.
    """
    def __init__(self, size):
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
