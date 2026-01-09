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
    data = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    # variables
    names = ['Farrah', 'Fred', 'Felicia']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']
    #plt.rcParams['lines.linewidth'] = 0.5

    # bar settings
    plt.bar(names, data[0], color='r', label=fruits[0], width = 0.5)
    plt.bar(names, data[1], color='y', width = 0.5,
            bottom=data[0], label=fruits[1])
    plt.bar(names, data[2], color='#ff8000', width = 0.5,
            bottom=data[0] + data[1], label=fruits[2])
    plt.bar(names, data[3], color='#ffe5b4', width = 0.5,
            bottom=data[0] + data[1] + data[2], label=fruits[3])

    # plot settings
    plt.ylim(0, 80)
    plt.yticks(range(0, 81, 10))
    plt.ylabel('Quantity of Fruit')
    plt.title('Number of Fruit per Person')
    plt.legend()
    plt.savefig('plot6.png')
    plt.show()
