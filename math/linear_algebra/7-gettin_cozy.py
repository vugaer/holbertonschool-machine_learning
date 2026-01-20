#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]

    # Checker
    conditions = (
        colrowdiff(m1) or
        colrowdiff(m2) or
        dimdiff(m1, m2, axis)
    )
    if conditions:
        return None

    # Main
    else:
        if not axis:  # axis == 0
            result += [row[:] for row in m2]
        elif axis:    # axis == 1
            for i in range(len(m1)):
                result[i] += m2[i][:]

    return result


def colrowdiff(m):
    """Returns True if matrix is empty / invalid / ragged, else False"""

    # must be a list
    if not isinstance(m, list):
        return True

    # empty matrix
    if len(m) == 0:
        return True

    # must be list of lists and no empty rows
    if not all(isinstance(row, list) for row in m):
        return True
    if any(len(row) == 0 for row in m):
        return True

    # rectangular check (no ragged rows)
    row_len = len(m[0])
    if any(len(row) != row_len for row in m):
        return True

    return False


def dimdiff(m1, m2, axis):
    """Returns True if dimensions do NOT match for concatenation, else False"""

    # axis must be 0 or 1
    if axis not in (0, 1):
        return True

    # at this point matrices are assumed non-empty rectangular (checked already)
    if not axis:  # axis == 0: columns must match
        return len(m1[0]) != len(m2[0])

    # axis == 1: rows must match
    return len(m1) != len(m2)
