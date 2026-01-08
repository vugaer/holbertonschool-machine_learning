#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    df1 = index(df1)
    df2 = index(df2)
    df1_new = df1.loc[
            (df1.index >= 1417411980) &
            (df1.index <= 1417417980)]
    df2_new = df2.loc[
            (df2.index >= 1417411980) &
            (df2.index <= 1417417980)]
    output = pd.concat([df2_new, df1_new], keys=['bitstamp', 'coinbase'])
    output = output.swaplevel(1, 0)
    return output.sort_index()
