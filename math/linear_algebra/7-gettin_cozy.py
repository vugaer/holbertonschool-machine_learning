#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    # Checker
    empty_matrix = [[], [[], []], [[], [], []]]
    conditions = colrowdiff(m2, axis) or m1 in empty_matrix or m2 in empty_matrix
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

def colrowdiff(m2, axis):
    """Returns True if m2 has inconsistent shape (ragged), else False"""

    # axis must be 0 or 1
    if axis not in (0, 1):
        return True

    # must be a list (matrix)
    if not isinstance(m2, list):
        return True

    # empty matrix is invalid
    if len(m2) == 0:
        return True

    lengths = []

    for row in m2:
        # each row must be a list
        if not isinstance(row, list):
            return True

        lengths.append(len(row))

    # if any row is empty -> invalid matrix
    if 0 in lengths:
        return True

    # ragged matrix check
    if len(set(lengths)) != 1:
        return True

    return False

