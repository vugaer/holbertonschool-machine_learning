#!/usr/bin/env python3

""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig?"""
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))
    plt.scatter(x, y, c='m')
    plt.xlabel('Height (in)')
    plt.ylabel('Weight (lbs)')
    plt.title("Men's Height vs Weight")
    plt.show()
    plt.savefig('plot2.png')
