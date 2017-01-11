#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    comp_list = my_list[0]
    for i in range(len(my_list)):
        if comp_list < my_list[i]:
            comp_list = my_list[i]
    return (comp_list)
