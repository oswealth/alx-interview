#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve 'n' characters.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get exactly
    'n' 'H' characters in the file.
    :param n: int
    :return: int
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
