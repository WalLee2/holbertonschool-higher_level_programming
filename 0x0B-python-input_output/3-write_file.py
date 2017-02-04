#!/usr/bin/python3
"""
Reading n lines of a text file in UTF-8 format and printing to standard out.
"""


def write_file(filename="", text=""):
    """
    Opening a text file in UTF-8 format and writing in the file.
    Opening the file in read mode and returning the number of characters.
    """
    with open(filename, mode="w", encoding="UTF-8") as my_file:
        my_file.write("Holberton School is so cool!\n")
    with open(filename, 'r', encoding="UTF-8") as my_file:
        c_count = 0
        for i in my_file:
            for j in i:
                c_count += 1
        return (c_count)
