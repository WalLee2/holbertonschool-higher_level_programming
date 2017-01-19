#!/usr/bin/python3
"""
Function that prints "My name is" and the first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    Checking if the first and last name are strings if not, it will produce
    an error.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
