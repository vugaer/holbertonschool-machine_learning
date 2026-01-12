#!/usr/bin/env python3
""" Apple's new idea: iSmile """


def summation_i_squared(n):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if (not isinstance(n, int)) and (n <= 0):
        return None
    else:
        squared = list(map(lambda x: x**2, range(1, int(n+1))))
        return sum(squared)
