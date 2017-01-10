#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cp_list = my_list[:]
    for i in range(len(cp_list)):
        if (i == idx):
            cp_list[i] = element
            return (cp_list)
    return (my_list)
