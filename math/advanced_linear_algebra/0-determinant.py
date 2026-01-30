#!/usr/bin/env python3

"""we are trying to find a determinant"""


def determinant(matrix):
    """asdasdasdasdasdasdasdasdasdasd
    asdasdasdasdasdasdasdasdasdasdasd
    asdasdasdasdasdasdasdasdasdasdasd"""
    # Extreme Cases
    if matrix == [[]]:
        return 1
    elif matrix == []:
        raise TypeError("matrix must be a list of lists")
    elif len(matrix[0]) == 1:
        return matrix[0][0]
    elif not all([isinstance(i, list) for i in matrix]):
        raise TypeError("matrix must be a list of lists")
    elif not all(len(srow) == len(matrix) for srow in matrix):
        raise ValueError("matrix must be a square matrix")
    # for 2x2
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    # for 3x3
    m1 = matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]
    m2 = matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0]
    m3 = matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]
    return matrix[0][0]*m1 - matrix[0][1]*m2 + matrix[0][2]*m3
