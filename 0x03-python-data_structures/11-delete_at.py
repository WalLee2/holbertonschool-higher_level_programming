#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return None
    for i in range(len(my_list)):
        if i == idx:
            my_list.remove(i + 1)
            return (my_list)
    return (my_list)
