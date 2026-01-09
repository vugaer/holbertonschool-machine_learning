#!/usr/bin/env python3

""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def bars():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig?"""

    np.random.seed(5)
    data = np.random.randint(0, 20, (4,3))
    plt.figure(figsize=(6.4, 4.8))

    names = ['Farrah', 'Fred', 'Felicia']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']

    df = pd.DataFrame(data, columns=names ,index=fruits).T
    df.plot(kind='bar', stacked=True)


    # plot settings
    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))
    plt.ylabel('Quantity of Fruit')
    plt.savefig('plot6.png')
