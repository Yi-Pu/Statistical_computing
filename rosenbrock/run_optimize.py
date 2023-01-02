# This file is the run the optimization function
# defined in the optimize_function module

from optimize_function import vec_optimize, non_vec_optimize
import time
import matplotlib.pyplot as plt
import numpy as np
import math

n_list = np.arange(100, 2100, 100)
a = math.pi / 2
b = 100

# Optimize function using vec_optimize
vec_time = []
vec_x = []
vec_y = []
vec_f = []
vec_dis = []
for n in n_list:
    # Keep time
    start_time = time.time()
    vec_list = vec_optimize(n)
    end_time = time.time()
    # Add the results to list
    vec_time.append(end_time - start_time)
    vec_x.append(vec_list[0])
    vec_y.append(vec_list[1])
    vec_f.append(vec_list[2])
    # Calculated distance
    dis = np.sqrt(
        (vec_list[0] - a) ** 2 +
        (vec_list[1] - a ** 2) ** 2)
    vec_dis.append(dis)
print(vec_time)  # Print computing time

# Optimize function using non_vec_optimize
non_vec_time = []
non_vec_x = []
non_vec_y = []
non_vec_f = []
non_vec_dis = []
for n in n_list:
    # Keep time
    start_time = time.time()
    non_vec_list = non_vec_optimize(n)
    end_time = time.time()
    # Add the results to list
    non_vec_time.append(end_time - start_time)
    non_vec_x.append(non_vec_list[0])
    non_vec_y.append(non_vec_list[1])
    non_vec_f.append(non_vec_list[2])
    # Calculated distance
    dis = np.sqrt(
        (non_vec_list[0] - a) ** 2 +
        (non_vec_list[1] - a ** 2) ** 2)
    non_vec_dis.append(dis)
print(non_vec_time)  # Print computing time

# A graph of computing time
plt.plot(
    n_list, vec_time, color="r",
    label="vectorized")
plt.plot(
    n_list, non_vec_time, color="b",
    label="non-vectorized")
plt.xlabel("n")
plt.ylabel("Computing Time")
plt.legend(loc="best")
plt.show()

# A graph of ratio
vec_time_arr = np.array(vec_time)
non_vec_time_arr = np.array(non_vec_time)
ratio = vec_time_arr/non_vec_time_arr
plt.plot(
    n_list, ratio, color="r",
    label="non-vectorized")
plt.xlabel("n")
plt.ylabel("Ratio")
plt.show()

# A graph of distance
plt.plot(
    n_list, vec_dis, color="r",
    label="vectorized")
plt.plot(
    n_list, non_vec_dis, color="b",
    label="non-vectorized")
plt.xlabel("n")
plt.ylabel("Distance")
plt.show()

# A graph of f across n
plt.plot(
    n_list, vec_f, color="r",
    label="vectorized")
plt.plot(
    n_list, non_vec_f, color="b",
    label="non-vectorized")
plt.xlabel("n")
plt.ylabel("Rosenbrock Function")
plt.show()

# Make a plot of f on 2D plane
n = 2000
# Partition intervals
x_interval = np.linspace(-3, 3, n+1)
y_interval = np.linspace(-1, 5, n+1)
# Vectorization
x_vec, y_vec = np.meshgrid(
    x_interval, y_interval)
# Calculate Rosenbrock function on a 2D plance
f = (a - x_vec) ** 2 + b * (y_vec - x_vec ** 2) ** 2
f_log = np.log(f)
h = plt.contourf(x_interval, y_interval, f_log)
plt.axis('scaled')
plt.colorbar()
plt.show()
