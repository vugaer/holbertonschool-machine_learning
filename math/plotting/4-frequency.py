#!/usr/bin/env python3

""" to be absolutely honest, what I am I have no idea
what the absolute f**k are these, I mean honestly
what absolute human prick would solve this question
without savefig?"""

import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """ to be absolutely honest, what I am I have no idea
    what the absolute f**k are these, I mean honestly
    what absolute human prick would solve this question
    without savefig?"""

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # plot the actual
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='k')  # color def & ec black

    # texts and stuff
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')
    plt.ylim(0, 30)  # case spesific
    plt.xlim(0, 100)  # without it 100 is not seen
    plt.xticks(range(0, 101, 10))
    # save and show
    plt.show()
    plt.savefig('plot5.png')
