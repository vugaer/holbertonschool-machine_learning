#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

import pandas as pd


def rename(df):
    """docstring lorem ipsum dolor sit amet
    holberton require s students to write
    useless stuff dot net"""
    df['Datetime'] = pd.to_datetime(df['Timestamp'], unit='s')
    return df[['Datetime', 'Close']]
