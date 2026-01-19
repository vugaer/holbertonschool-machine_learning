#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    if not axis:
        result.append([m2[i] for i in range(len(m2))])
    print('#############################')
    print(f'm1={m1}\nm2={m2}\naxis={axis}')
    return result
