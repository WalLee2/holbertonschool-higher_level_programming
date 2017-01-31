#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Class Square that inherits from Rectangle
"""


class Square(Rectangle):

    """
    Defining Square, initiating an instance of size, creating a method area.
    """

    def __init__(self, size):
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size
