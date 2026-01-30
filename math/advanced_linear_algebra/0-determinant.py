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

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    j = 0
    while j < n:
        a = matrix[0][j]

        minor = []
        r = 1
        while r < n:
            row = []
            c = 0
            while c < n:
                if c != j:
                    row.append(matrix[r][c])
                c += 1
            minor.append(row)
            r += 1

        sign = -1 if (j % 2 == 1) else 1

        det += sign * a * determinant(minor)
        j += 1

    return det
