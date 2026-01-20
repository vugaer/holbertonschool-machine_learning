#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    # Checker
    empty_matrix = [[], [[], []], [[], [], []]]
    conditions = any([len(m1) < len(m2), m1 in empty_matrix, m2 in empty_matrix])
    if conditions:
        return None
    # Main
    else:
        if not axis:
            result += [m2[i] for i in range(len(m2))]
        elif axis:     
            for i in range(len(m2)):
                result[i] += m2[i]
    # print('#############################')  # for Debug
    # print(f'm1={m1}\nm2={m2}\naxis={axis}')
    return result


