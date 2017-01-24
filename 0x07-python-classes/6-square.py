#!/usr/bin/python3
"""
Creating a class named square with a private instance attribute.
Defining another function within the class that finds the square of size.
Printing boxes with "#" symbol.
"""


class Square:
    """
    initiates the variable self, size, and position
    made a public instance method returning square area
    public instance method returning a square of size "size" where size
    is the number passed to the function.
    """

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

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

    def my_print(self):
        if (self.__size == 0):
            print('\n')
        if self.position[1] >= 1 and self.size is not 0:
            print('\n' * int(self.position[1]))
        for i in range(0, int(self.__size)):
            if self.position[0] >= 0:
                print("{}{}".format(' ' * int(self.position[0]),
                                    "#" * int(self.__size)))
