#!/usr/bin/env python3


""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt


def change_scale():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig?"""
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)
    plt.figure(figsize=(6.4, 4.8))
    plt.plot(x, y, 'b')
    plt.title('Exponential Decay of C-14')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.xlim(0, 28650)
    plt.yscale('log')
    plt.show()
    plt.savefig('plot3.png')
