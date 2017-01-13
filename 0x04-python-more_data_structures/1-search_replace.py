#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function that replaces all occurences of
    an element by another in a new list.
    """
    return[replace if search == i else i for i in my_list]
