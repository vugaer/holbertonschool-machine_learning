#!/usr/bin/env python3
""" Apple's new idea: iSmile """


def poly_integral(poly, C=0):
    """ we will create a program that will
    end future developer's j*b... let's go """
    # npoly # 5x^0 + 3x^1 + 0x^2 + 1x^3  [5, 3, 0, 1]
    # poly  # C + 5x^1 + 1.5x^2 + 0x^3 + 0.25x^4 [C, 5, 1.5 ,0, 0.25]
    if isinvalid_poly(poly) or isinvalid_c(C):
        return None
    else:
        npoly = [C] + [0] * len(poly)
        for i in range(1, len(npoly)):
            npoly[i] = poly[i-1]/i
        return npoly


def isinvalid_poly(poly):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if isinstance(poly, list):
        if not poly:
            return True
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


def isinvalid_c(c):
    """ we will create a program that will
    end future developer's j*b... let's go """
    if not isinstance(c, int):
        return True
    return False
