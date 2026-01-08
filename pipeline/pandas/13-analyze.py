#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""


def analyze(df):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    return df.drop(['Timestamp'], axis=1).describe()
