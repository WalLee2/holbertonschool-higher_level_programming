#!/usr/bin/python3
"""
Reading n lines of a text file and prints to standard out.
"""


def read_lines(filename="", nb_lines=0):
    """
    Opening the file and reading everything if nb_lines is less than 0
    or greater than the LineCount
    """
    with open(filename, 'r', encoding="UTF-8") as my_file:
        lineCount = 1
        for i in my_file:
            lineCount += 1
    with open(filename, 'r', encoding="UTF-8") as my_file:
        if nb_lines <= 0 or nb_lines >= lineCount:
            print(my_file.read(), end="")
        else:
            for line in range(0, nb_lines):
                print(my_file.readline(), end="")
