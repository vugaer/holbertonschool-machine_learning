#!/usr/bin/env python3
""" Apple's new idea: iSmile """


def summation_i_squared(n, i=1):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if type(n) is not int:
        return None
    else:
        squared = list(map(lambda x: x**2, range(i, n+1)))
        return sum(squared)
