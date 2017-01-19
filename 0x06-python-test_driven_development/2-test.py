#!/usr/bin/python3
"""

"""


def matrix_divided(matrix, div):

    try:
        if div is 0:
            raise ZeroDivisionError("division by zero")
        if matrix is not None and div is not 0:
            return list((round(j / div, 2) for i in matrix for j in i))
