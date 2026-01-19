#!/usr/bin/env python3

"""Module Documentation Lorem Ipsum"""


def add_matrices2D(arr1, arr2):
    """Look at the functions first,
    then this one! Good practice!"""
    if any([arr1 == [[], []], arr1 == [], not arr1, arr1 == None]):
        return []
    elif not checkshape(arr1, arr2):
        return None
    else:
        newarr = []
        for i, j in zip(arr1, arr2):
            newarr += [sum2dmatrix(i, j)]
        return newarr


def checkshape(arr1, arr2):
    """We check the shape of two arrays.
    To eliminate repetition, we import them"""
    matrix_shape = __import__('2-size_me_please').matrix_shape
    return (matrix_shape(arr1) == matrix_shape(arr2))


def sum2dmatrix(arr1, arr2):
    """ sum 2d matrixes with each other"""
    if isinstance(arr1, list):
        sumarr = arr1.copy()
        for i in range(len(arr1)):
            sumarr[i] = arr1[i] + arr2[i]
        return sumarr
    if isinstance(arr1, (int, float)):
        return arr1 + arr2
