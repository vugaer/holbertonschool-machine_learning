#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    if not axis:
        if isinstance(m2[0], int):
            result += [m2]
        elif isinstance(m2[0], list):
            result += [m2[i] for i in range(len(m2))]
        # else:
        #     for i in len(m2):
        #         result += [m2[i]]
    if axis:
        return None

    return result
