#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(mat1, mat2, axis=0):
    """asdasdasdasdasasasdasasd
    asasdasasdasdasdasdasdasdasd"""
    result = mat1[:]
    if axis == 0:
        result += [_ for _ in mat2]
    if axis == 1:
        for i in range(len(mat2)):
            result[i] += [mat2[i][0]]
    return result
