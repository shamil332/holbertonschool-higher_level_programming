#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[(lambda x: x * x)(x) for x in row] for row in matrix]
