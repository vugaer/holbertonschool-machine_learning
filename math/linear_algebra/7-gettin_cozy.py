#!/usr/bin/env python3

""" I REALLY DON'T RECOMMEND WRITING THIS ON YOUR
OWN, THIS IS COMPLETELY BULLSHIT QUESTION BASED ON
SOMEONE'S FUCKING STUPID EGO. I WASTED MY SHITTY
5 FUCKING HOURS ON THAT STUPID IDIOTIC QUESTION
WHILE WE JUST HAVE NP.CONCAT(). AT LEAST GIVE
REASONABLE QUESTIONS NOT BULLSHIT LIKE THIS"""


def cat_matrices2D(m1, m2, axis=0):
    """LOREM IPSUM DOLOR FUCK WHOEVER WROTE THIS QUESTION
    LOREM IPSUM DOLOR FUCK WHOEVER WROTE THIS Q"""
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
    return False


def dimdiff(m1, m2, axis):
    """LOREM IPSUM DOLOR FUCK WHOEVER WROTE THIS QUESTION
    LOREM IPSUM DOLOR FUCK WHOEVER WROTE THIS Q"""
    if not axis:  # axis=0
        return len(m1[0]) != len(m2[0])
    return len(m1) != len(m2)  # axis=1
