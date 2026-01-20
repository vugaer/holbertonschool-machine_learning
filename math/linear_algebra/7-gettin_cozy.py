#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    if not checker(m1, m2):
        return None
    else:
        if not axis:
            result += [m2[i] for i in range(len(m2))]
        elif axis:     
            for i in range(len(m2)):
                result[i] += m2[i]
    # print('#############################')  # for Debug
    # print(f'm1={m1}\nm2={m2}\naxis={axis}')
    return result

def checker(m1, m2):
    matrix_shape = __import__('2-size_me_please').matrix_shape
    return matrix_shape(m1) == matrix_shape(m2)
