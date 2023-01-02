# This file is to test if the functions \
# in optimize_function module work correctly

from optimize_function import vec_optimize, non_vec_optimize
import math
import numpy as np
import pytest

# Set n and a
n = 2000
a = math.pi / 2


def test_vec_optimize():
    # This is to test the vec_optimize function
    vec_list = vec_optimize(n)
    # Check if the minimizer is around (a, a^2)
    dis = np.sqrt(
        (vec_list[0] - a) ** 2 +
        (vec_list[1] - a ** 2) ** 2)
    assert dis < 0.05
    # Check if the min value is close to 0
    assert vec_list[2] < 0.0001


def test_non_vec_optimize():
    # This is to test the non_vec_optimize function
    non_vec_list = non_vec_optimize(n)
    # Check if the minimizer is around (a, a^2)
    dis = np.sqrt(
        (non_vec_list[0] - a) ** 2 +
        (non_vec_list[1] - a ** 2) ** 2)
    assert dis < 0.05
    # Check if the min value is close to 0
    assert non_vec_list[2] < 0.0001


def test_errors():
    # This is to test if both the two
    # methods raise errors correctly
    with pytest.raises(ValueError):
        vec_optimize(-1)
        vec_optimize(10.6)
        non_vec_optimize(-1)
        non_vec_optimize(10.6)
