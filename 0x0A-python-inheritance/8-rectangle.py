#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Rectangle class that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Inheriting from BaseGeometry
    """
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
