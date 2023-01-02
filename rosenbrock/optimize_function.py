# This file is to define the fuctions that can
# find the optimal point of Rosenbrock function

import math
import numpy as np


def vec_optimize(n):
    # This function is to use NumPy functionality to
    # perform the evaluation in a vectorized manner

    # Raise error of n in not valid
    if (n < 1) or not isinstance(n, int):
        raise ValueError("you should input a valid n")

    # Set variables
    a = math.pi / 2
    b = 100

    # Partition intervals
    x_interval = np.linspace(-3, 3, n+1)
    y_interval = np.linspace(-1, 5, n+1)

    # Vectorization
    x_vec, y_vec = np.meshgrid(
        x_interval, y_interval)

    # Calculate Rosenbrock function on a 2D plance
    f = (a - x_vec) ** 2 + b * (y_vec - x_vec ** 2) ** 2

    # Look for the optimal point and function value
    f_min = np.amin(f)
    res = np.where(f == f_min)
    x_best = x_interval[res[1]][0]
    y_best = y_interval[res[0]][0]

    return [x_best, y_best, f_min]


def non_vec_optimize(n):
    # This function is to perform the
    # evaluation in a non-vectorized manner

    if (n < 1) or not isinstance(n, int):
        raise ValueError("you should input a valid n")

    # Set variables
    a = math.pi / 2
    b = 100

    # Partition intervals
    x_interval = np.linspace(-3, 3, n+1)
    y_interval = np.linspace(-1, 5, n+1)

    # Initialize optimal point and function value to be reported
    x_best = x_interval[0]
    y_best = y_interval[0]
    f_min = (a - x_best) ** 2 +\
        b * (y_best - x_best ** 2) ** 2

    # Use double loop to find the optimal point
    for x in x_interval:
        for y in y_interval:
            f = (a - x) ** 2 + b * (y - x ** 2) ** 2
            if f < f_min:
                x_best = x
                y_best = y
                f_min = f

    return [x_best, y_best, f_min]
