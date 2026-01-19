#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    if not axis:
        if len(m2) == 1:
            result += [m2[0]]
        else:
            for i in len(m2):
                result += [m2[i]]
    if axis:
        return None

    return result
