#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

import pandas as pd
from datetime import datetime


def rename(df):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    df['Timestamp'] = df['Timestamp'].apply(datetime.fromtimestamp)
    return df
