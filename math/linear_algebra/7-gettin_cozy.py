#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    # Checker
    empty_matrix = [[], [[], []], [[], [], []]]
    conditions = coldiff(m2) or m1 in empty_matrix or m2 in empty_matrix
    if conditions:
        return None
    # Main
    else:
        if not axis:
            result += [m2[i] for i in range(len(m2))]
        elif axis:
            for i in range(len(m1)):
                result[i] += m2[i]
    # print('#############################')  # for Debug
    # print(f'm1={m1}\nm2={m2}\naxis={axis}')
    return result

def coldiff(m2):
    """ Column Match Tool for Checker """
    lengths = []
    for i in m2:
        if isinstance(i, (int, float)):
            lengths += [1]
        elif isinstance(i, list):
            lengths += [len(i)]
    if len(set(lengths)) == 1:
        return False
    else:
        return True
