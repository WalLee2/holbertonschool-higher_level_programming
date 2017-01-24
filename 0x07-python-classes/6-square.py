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
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) && not position[0] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int) && not position[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if (self.size == 0):
            print('\n')
            return
        if self.position[1] >= 1 and self.__size is not 0:
            print("{}".format('\n' * int(self.position[1])), end="")
        for i in range(0, int(self.__size)):
            if self.position[0] >= 0:
                print("{}{}".format(' ' * int(self.position[0]),
                                    "#" * int(self.__size)))
