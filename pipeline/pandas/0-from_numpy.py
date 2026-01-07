#!/usr/bin/env python3

import pandas as pd

"""Write a function def from_numpy(array): that creates a pd.DataFrame from a np.ndarray:

array is the np.ndarray from which you should create the pd.DataFrame
The columns of the pd.DataFrame should be labeled in alphabetical order and capitalized. There will not be more than 26 columns.
Returns: the newly created pd.DataFrame"""

def from_numpy(array):
    
    """ we can use chr for the alphabet starts from 65 """

    return pd.DataFrame(columns=[chr(65 + i) for i in range(len(array[0]))], data=array)
