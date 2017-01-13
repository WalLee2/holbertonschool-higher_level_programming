#!/usr/bin/python3
def multiply_by_2(my_dict):
    """
    Function that returns a new dictionary with all values multiplied by 2
    """
    new_dict = my_dict.copy()
    for k, v in new_dict.items():
        new_dict.update({k : (v * 2)})
    return new_dict
