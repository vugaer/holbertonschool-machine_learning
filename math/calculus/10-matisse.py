#!/usr/bin/env python3
""" Apple's new idea: iSmile """


def poly_derivative(poly):
    """ we will create a program that will
    end future developer's j*b... let's go """
    # npoly # 5x^0 + 3x^1 + 0x^2 + 1x^3  [5, 3, 0, 1]
    # poly  # 3x^0 + 0x^1 + 3x^2 + 0x^3  [3, 0, 3, 0]
    if isinvalid(poly):
        return None
    else:
        npoly = [0] * len(poly)
        for i in range(1, len(poly)):
            npoly[i-1] = poly[i]*i
        if npoly == [0]:
            return [0]
        return npoly[:-1]

def isinvalid(poly):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if isinstance(poly, list):
        notint = False
        for i in poly:
            if not isinstance(i, int):
                notint = True
        if notint:
            return True
        else:
            return False
    else:
        return True
