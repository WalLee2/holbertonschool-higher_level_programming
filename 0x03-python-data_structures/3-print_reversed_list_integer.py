#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        i += 48
        print(str.format(chr(i)))
