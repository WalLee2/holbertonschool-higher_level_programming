#!/usr/bin/python3
"""
Expanding 0-rectangle to include:
A private width attribute
A private hieght attribute
"""


class Rectangle:
    """
    Instantiating width and height to private variables
    Using getter and setter to retrieve the value stored at self.width and
    self.height and checking the value being passed to width and height before
    setting it.
    """

    def __init__(self, width=0, height=0):
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int) or\
           isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
