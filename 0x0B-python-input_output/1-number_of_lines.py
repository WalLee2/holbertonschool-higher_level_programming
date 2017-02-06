#!/usr/bin/python3
"""
Return the number of lines of a text file.
"""


def number_of_lines(filename=""):
    """
    Open file and add 1 to counter for each line read.
    """
    with open(filename, 'r', encoding="UTF-8") as my_file:
        lineCount = 0
        while True:
            line = my_file.readline()
            if not line:
                break
            lineCount += 1
        return (lineCount)
