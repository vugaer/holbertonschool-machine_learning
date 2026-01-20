#!/usr/bin/env python3

"adsadasadasdadasdasdasdasdadadadsad
asdasdasdadasdasdasdasdasdasdasdasasd
WASTED_HOURS = 6 hours"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    # Checker
    conditions = matdiff(m1) or matdiff(m2) or dimdiff(m1, m2, axis)
    if conditions:
        return None
    # Main
    else:
        if not axis:  # axis == 0
            result += [row[:] for row in m2]   # copy m2 rows
        elif axis:    # axis == 1
            for i in range(len(m1)):
                result[i] += m2[i][:]          # copy slice
    return result

def matdiff(m):
    """FUCK WHOEVER EVER THOUGHT OF THIS QUESTION
    WTF IS THAT??? ARE YOU INSANE? FUCK YOU!!!"""
    if not isinstance(m, list) or len(m) == 0:
        return True
    if not all(isinstance(row, list) for row in m):
        return True

    # # rectangular check (allow row length 0)
    # row_len = len(m[0])
    # for row in m:
    #     if len(row) != row_len:
    #         return True

    return False


def dimdiff(m1, m2, axis):
    # """Return True if dimensions do NOT match for concatenation."""
    # if axis not in (0, 1):
    #     return True

    if not axis:  # axis == 0: columns must match (including 0)
        return len(m1[0]) != len(m2[0])

    # axis == 1: rows must match
    return len(m1) != len(m2)
