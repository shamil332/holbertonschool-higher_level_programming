#!/usr/bin/python3
"""module for task 12"""


def pascal_triangle(n):
    """return pascal triangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[i-1]
        f = [1]
        for j in range(1, i):
            f.append(prev[j-1] + prev[j])

        f.append(1)
        triangle.append(f)

    return triangle
