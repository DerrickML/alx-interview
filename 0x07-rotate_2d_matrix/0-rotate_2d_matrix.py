#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    N = len(matrix)

    for i in range(N):
        for j in range(i, N):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(N):
        for j in range(N // 2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][N - 1 - j]
            matrix[i][N - 1 - j] = temp
