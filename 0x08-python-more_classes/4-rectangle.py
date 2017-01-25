#!/usr/bin/python3
"""
Expanding 3-rectangle to include:
Using __repr__ to print out the what the given the name of the class along with
height and width values
"""


class Rectangle:
    """
    Returning the class name with height and width values
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
        if not isinstance(self.__height, int) or \
           isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        product = ""
        for i in range(0, self.__height):
            product = (product + ("#" * int(self.__width)))
            product = product + '\n'
        product = product.strip('\n')
        return product

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
