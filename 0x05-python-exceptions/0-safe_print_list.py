#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Function that prints x elements of a list.
    """
    try:
        count = 0
        new_list = []
        for i in range(0, x):
            if count < x:
                new_list.append(my_list[i])
            count += 1
        print(*new_list, sep="")
        return (count)
    except IndexError:
        print(*new_list, sep="")
        return (count)
