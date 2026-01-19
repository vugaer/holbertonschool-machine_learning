#!/usr/bin/env python3
""" simple flask application (no!) """

def matrix_shape(matrix):
    """ lorem ipsum dolor sit amet
    lets do sumthing that will make worse """
    shape = []
    while isinstance(matrix, list):
        shape += [len(matrix)]
        matrix = matrix[0]
    return shape
