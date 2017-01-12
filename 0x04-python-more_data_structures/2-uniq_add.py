#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Function that makes the addition of all unique integers in a list.
    """
    uniq_list = set(my_list)
    result = 0
    for i in uniq_list:
        result = result + i
    return result
