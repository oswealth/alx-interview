#!/usr/bin/python3
"""
Rotate an n x n 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): The matrix to be rotated.

    Returns:
    None: The function modifies the matrix in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
