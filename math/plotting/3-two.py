#!/usr/bin/env python3

""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt


def two():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig """

    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    # plot itself

    plt.plot(x, y1, label='C-14', color='red', linestyle='dashed')
    plt.plot(x, y2, color='green', label='Ra-226')

    # title labels and limitation

    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # show and legend

    plt.legend(loc='upper right')  # I have been working for ts
    plt.show()
    plt.savefig('plot4.png')
