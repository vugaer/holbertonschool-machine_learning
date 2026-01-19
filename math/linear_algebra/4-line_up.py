#!/usr/bin/env python3
import numpy as np

"""Module Documentation Lorem Ipsum"""


def add_arrays(arr1, arr2):
    """Yuxularımı o atır suya, mənim üçün elə sino
    gedir guya (:d) lorem ipsum dolor sit amet"""
    if not checkshape(arr1, arr2):
        return None
    return np.array(arr1) + np.array(arr2)

def checkshape(arr1, arr2):
    """Yuxularımı o atır suya, mənim üçün elə sino
    gedir yuya (:d) lorem ipsum dolor sit amet"""
    matrix_shape = __import__('2-size_me_please').matrix_shape
    return matrix_shape(arr1) == matrix_shape(arr2)
