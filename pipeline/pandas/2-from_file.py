#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

import pandas as pd

def from_file(filename, delimiter):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    return pd.read_csv(filepath_or_buffer=filename, delimiter=delimiter)
