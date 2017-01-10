#!/usr/bin/python3
def replace_in_list(list, idx, element):
    for i in range (len(list)):
        if (i == idx):
            list[i] = element
            return (list)
