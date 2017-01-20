#!/usr/bin/python3
"""
Dividing all numbers in the matrix by the number passed to div with the
outcome being rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    If the matrix is not an int or a float raise an error
    If the length of each row is not the same raise an error
    If div is 0 raise an error
    If div is anything but an int or float raise an error
    """

    if not matrix:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if not all(len(k) == len(matrix[0]) for k in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(len(k) > 0 for k in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if not all(isinstance(k, (int, float)) for k in row):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
    return(list(round(j / div, 2) for i in matrix for j in i if div is not 0))
