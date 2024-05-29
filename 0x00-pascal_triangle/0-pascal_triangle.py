#!/usr/bin/python3
"""Generates Pascal's Triangle up to the nth row"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        # Calculate the inner elements of the new row
        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            new_row.append(value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
