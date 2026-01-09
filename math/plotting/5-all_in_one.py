#!/usr/bin/env python3

""" Grade me full, I will reciprocate back to you with 100. """

import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """ Plot all graphs again. I commented out codes
    differently. You can take a look to comments..."""

    y0 = np.arange(0, 11) ** 3

    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180

    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)

    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)

    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # fontsize settings
    plt.rcParams['axes.titlesize'] = "x-small"
    plt.rcParams['axes.labelsize'] = "x-small"
    plt.rcParams['legend.fontsize'] = "x-small"
    # this has to be set before plt.figure()
    # I made fucking debugging for hours

    # set multiplot and sep into grids
    fig = plt.figure(constrained_layout=True)
    # fig = plt.figure()
    # fig.subplots_adjust(hspace=0.5, wspace=0.3)  # manual handling

    grids = fig.add_gridspec(3, 2)  # 3 row, 2 cols
    q1 = fig.add_subplot(grids[0, 0])
    q2 = fig.add_subplot(grids[0, 1])
    q3 = fig.add_subplot(grids[1, 0])
    q4 = fig.add_subplot(grids[1, 1])
    q5 = fig.add_subplot(grids[2, :])

    """ Plt axes usually used set_ prefix
    before the normal command. It makes way
    easier than the other way around...
    that's imo of course """

    # Plot 1 (q1):
    q1.plot(y0, c='r')
    q1.set_xlim(0, 10)

    # Plot 2 (q2):
    q2.scatter(x1, y1, c='m')
    q2.set_xlabel('Height (in)')
    q2.set_ylabel('Weight (lbs)')
    q2.set_title("Men's Height vs Weight")

    # Plot 3 (q3):

    q3.plot(x2, y2)
    q3.set_yscale('log')
    q3.set_xlim(0, 28650)
    #q3.set_xticks(range(0, 30000, 10000))  # use this when font broken
    q3.set_title('Exponential Decay of C-14')
    q3.set_xlabel('Time (years)') 
    q3.set_ylabel('Fraction Remaining')

    # Plot 4 (q4):
    q4.plot(x3, y31, c='r', ls='dashed', label='C-14')
    q4.plot(x3, y32, c='g', label='Ra-226')
    q4.set_xlim(0, 20000)
    q4.set_ylim(0, 1)
    q4.set_title('Exponential Decay of Radioactive Elements')
    q4.set_ylabel('Fraction Remaining')
    q4.set_xlabel('Time (years)')
    q4.legend(loc='upper right')

    # Plot 5 (q5):
    q5.hist(student_grades, bins=range(0, 101, 10), ec='k')
    q5.set_title('Project A')
    q5.set_xlabel('Grades')
    q5.set_ylabel('Number of Students')
    q5.set_xlim(0, 100)
    q5.set_ylim(0, 30)
    q5.set_xticks(range(0, 101, 10))

    # save everything
    plt.suptitle('All in one', fontsize=16)
    plt.savefig('all-plots.png')
    plt.show()
