"""This file is to test if my functions are defined correctly."""

import numpy as np
from my_lin_alg import my_transpose, my_mat_prod
import sys
# The command below allows you to call my_transpose and my_mat_prod as if they
# were functions defined within this module
sys.path.append('/Users/yipu/statistical_computing/my_lin_alg-Yi-Pu')
# 5x3 matrix
X = np.array(
    [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9],
     [1, 4, 2],
     [3, 11, 5]])
# 3x4 matrix
Y = np.array(
    [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]])

# Add here code to compare your implementations of my_transpose and my_mat_prod
# against the comparable implementations from numpy
# Compare my_transpose and np.transpose
my_transpose(X)
np.transpose(X)
# Compare my_mat_prod and np.dot
my_mat_prod(X, Y)
np.dot(X, Y)
