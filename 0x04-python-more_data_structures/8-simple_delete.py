#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    """
    Function that delets a key in a dictionary.
    """
    if key in my_dict:
        del my_dict[key]
    return my_dict
