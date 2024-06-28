#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if the given data set represents
    a valid UTF-8 encoding.

    :param data: List of integers
    :return: Boolean indicating whether the data is a valid UTF-8 encoding
    """
    n_bytes = 0
    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask >>= 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if num >> 6 != 0b10:
                return False
        n_bytes -= 1
    return n_bytes == 0
