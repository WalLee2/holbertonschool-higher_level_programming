#!/usr/bin/python3
def multiply_by_2(my_dict):
    """
    Function that returns a new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for k in my_dict:
        new_dict.update({k: (my_dict[k] * 2)})
    return new_dict
