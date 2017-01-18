#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list((round(j / div, 2) for j in i if div is not 0)))
    return new_matrix
