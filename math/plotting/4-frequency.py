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
    bins = range(0, int(max(student_grades)) + 10, 10) # make 10 bins
    plt.hist(student_grades, bins=bins, edgecolor='k')  # color def & ec black

    # texts and stuff
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # save and show
    plt.show()
    plt.savefig('plot5.png')
    print(bins)
