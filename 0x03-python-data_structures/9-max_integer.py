#!/usr/bin/python3
def max_integer(my_list=[]):
    comp_list = 0
    if my_list is not None:
        for i in range(len(my_list)):
            comp_list = my_list[i]
            if comp_list < my_list[i + 1]:
                comp_list = my_list[i + 1]
            else:
                continue
        return (comp_list)
    return None
