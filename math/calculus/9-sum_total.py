#!/usr/bin/env python3
""" Apple's new idea: iSmile """


def summation_i_squared(n, i=1):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if type(n) is not int:
        return None
    else:
        cem = 0
        for x in range(i, n+1):
            cem += x**2
        return cem
