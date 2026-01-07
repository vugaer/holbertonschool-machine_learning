import pandas as pd

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""

my_dict = {"First": [0.0, 0.5, 1.0, 1.5], "Second": ["one", "two", "three", "four"]}

def from_dictionary(dict=my_dict):
    df = pd.DataFrame(my_dict, index=["A", 'B', 'C', 'D'])
    return df
