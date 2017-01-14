#!/usr/bin/python3
def safe_print_integer(value):
    """
    Function that prints an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
