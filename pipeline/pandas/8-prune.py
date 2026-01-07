#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

import pandas as pd


def prune(df):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    return df.dropna(subset=['Close'])
    
