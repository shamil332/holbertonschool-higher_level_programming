#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x*x
    return [[square(x) for x in row] for row in matrix]
