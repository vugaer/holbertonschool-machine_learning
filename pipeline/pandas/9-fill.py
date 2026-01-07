#!/usr/bin/env python3

"""docstring lorem ipsum dolor sit amet
holberton requires students to write
useless stuff dot net"""


def fill(df):
    """docstring lorem ipsum dolor sit amet
    holberton requires students to write
    useless stuff dot net"""
    # new df and rm Weighted_Price
    df_new = df.drop(['Weighted_Price'], axis=1)
    # ffill close column
    df_new['Close'] = df_new['Close'].ffill()
    # fill columns from close
    df_new['High'] = df_new['High'].fillna(df_new['Close'])
    df_new['Low'] = df_new['Low'].fillna(df_new['Close'])
    df_new['Open'] = df_new['Open'].fillna(df_new['Close'])
    # fillna with 0
    cols = ['Volume_(BTC)', 'Volume_(Currency)']
    df_new[cols] = df_new[cols].fillna(0)
    # that's enough
    return df_new
