#!/usr/bin/env python3

import pandas as pd
index = __import__('10-index').index

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""


def concat(df1, df2):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    # change index
    df1 = index(df1)
    df2 = index(df2)
    # limit
    df2_new = df2.loc[df2.index <= 1417411920]
    result = pd.concat([df2_new, df1], keys=["bitstamp", "coinbase"])
    return result
