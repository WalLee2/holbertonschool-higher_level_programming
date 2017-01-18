#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    try:
        if (isinstance(first_name, str) is False):
            raise TypeError("first_name must be a string")
        elif (isinstance(last_name, str)) is False:
            raise TypeError("last_name must be a string")
        else:
            print('My name is {:s} {:s}'.format(first_name, last_name))

    except TypeError as err:
        print(err)
