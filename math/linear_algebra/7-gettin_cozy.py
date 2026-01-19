#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    if not axis:
        result += [notrawlist(m2)]
    if axis:
        return None
    return result


def notrawlist(matrix):
    if len(matrix) == 1:
        return matrix[0]
    else:
        return matrix[:]
