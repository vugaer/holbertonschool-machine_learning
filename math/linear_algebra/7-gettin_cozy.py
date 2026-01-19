#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(mat1, mat2, axis=0):
    """asdasdasdasdasasasdasasd
    asasdasasdasdasdasdasdasdasd"""
    result = [row[:] for row in mat1]
    print(mat1, mat2)
    if axis == 0:
        result += [row[:] for row in mat2]
    if axis == 1:
        for i in range(len(mat2)):
            result[i] += [mat2[i][0]]
    #return result
