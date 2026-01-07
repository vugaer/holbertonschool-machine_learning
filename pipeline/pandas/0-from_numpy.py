#!/usr/bin/env python3

import pandas as pd

"""we can use chr for the alphabet starts from 65 lorem ipsum dolor sit amet"""


def from_numpy(array):
    """ we can use chr for the alphabet starts from 65 """

    cols = [chr(65 + i) for i in range(len(array[0]))]

    return pd.DataFrame(columns=cols, data=array)
