#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Function that replaces all occurences of
    an element by another in a new list.
    """
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list.pop(new_list[i])
            new_list.insert(i, replace)
    return (new_list)
