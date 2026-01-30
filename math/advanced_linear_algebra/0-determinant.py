#!/usr/bin/env python3

"""we are trying to find a determinant"""


def determinant(matrix):
    """asdasdasdasdasdasdasdasdasdasd
    asdasdasdasdasdasdasdasdasdasdasd
    asdasdasdasdasdasdasdasdasdasdasd"""
    # Extreme Cases
    if matrix == [[]]:
        return 1
    elif matrix == [] or not all([isinstance(i, list) for i in matrix]):
        raise TypeError("matrix must be a list of lists")
    elif not all(len(srow) == len(matrix) for srow in matrix):
        raise ValueError("matrix must be a square matrix")
    if len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        return round(np.linalg.det(matrix))
