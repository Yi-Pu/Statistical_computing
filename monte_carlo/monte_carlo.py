#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:30:44 2022

@author: yipu

This file is to use Monte Carlo Method to estimate pi
"""

import numpy
import math
import matplotlib.pyplot as plt

# Esimation list of pi
pi_list = []

for n in [10, 100, 1000, 10000, 100000, 1000000]:
    dat = numpy.random.rand(n, 2)
    I_n = 0
    for k in range(len(dat)):
        temp = dat[k][1] * dat[k][1] + dat[k][0] * dat[k][0]
        temp = math.pow(temp, 0.5)
        if (temp <= 1):
            I_n += 1
    pi = 4 * I_n / n
    pi_list.append(pi)
    print("When n =", n, "pi_hat = ", pi)
X = range(1, 7)
plt.plot(X, pi_list)
plt.hlines(math.pi, 1, 6,
           colors="r",
           linestyles="dashed")
plt.xlabel('$log_{10}(n)$')
plt.ylabel('pi_hat')
plt.title('Estimated pi$')
plt.savefig('Estimated_pi.pdf')
plt.show()
