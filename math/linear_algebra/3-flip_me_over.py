#!/usr/bin/env python3
""" simple flask application (no!) """


def matrix_transpose(matrix):
    """ lorem ipsum dolor sit amet
    this code does Transpose """
    transpose = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(transpose)):
        for j in range(len(transpose[0])):
            transpose[i][j] = matrix[j][i]
    return transpose
