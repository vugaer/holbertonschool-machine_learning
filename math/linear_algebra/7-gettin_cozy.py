#!/usr/bin/env python3

"adsadasadasdadasdasd"


def cat_matrices2D(m1, m2, axis=0):
    result = [row[:] for row in m1]
    # Checker
    if False:
        pass
    # Main
    else:
        if not axis:
            result += [m2[i] for i in range(len(m2))]
        elif axis:     
            for i in range(len(m2)):
                result[i] += m2[i]
    print('#############################')  # for Debug
    print(f'm1={m1}\nm2={m2}\naxis={axis}')
    return result
