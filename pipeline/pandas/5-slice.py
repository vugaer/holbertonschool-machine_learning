#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""


def slice(df):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
