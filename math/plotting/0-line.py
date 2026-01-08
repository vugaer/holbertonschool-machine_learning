#!/usr/bin/env python3

""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt


def line():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig?"""
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    x = np.arange(0, 11)
    plt.plot(x, y, 'r')
    plt.xlim(0, 10)
    plt.show()
    plt.savefig('plot.png')
