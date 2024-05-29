#!/usr/bin/python3
"""
Pascals triangle method
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the Pascals
    triangle of n
    """
    new_list = []
    if n > 0:
        for i in range(n):
            new_list.append([])
            new_list[i].append(1)
            for j in range(1, i):
                new_list[i].append(new_list[i - 1][j - 1] + new_list[i - 1][j])
            if i != 0:
                new_list[i].append(1)

    return new_list