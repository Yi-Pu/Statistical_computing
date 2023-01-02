# Implement your unit tests in this file

from find_interval import find_interval
import pytest
import numpy as np


def test_find_interval_regular_values():
    assert find_interval(1.2, [1.0, 2.0, 3.0, 4.0]) == 0
    assert find_interval(0.2, [1.0, 2.0, 3.0, 4.0]) == -1
    assert find_interval(3.5, [1.0, 2.0, 3.0, 4.0]) == 2
    assert find_interval(5.0, [1.0, 2.0, 3.0, 4.0]) == 3


def test_find_interval_edge_values():
    assert find_interval(1, [1.0, 2.0, 3.0, 4.0]) == 0
    assert find_interval(2, [1.0, 2.0, 3.0, 4.0]) == 1
    assert find_interval(3, [1.0, 2.0, 3.0, 4.0]) == 2
    assert find_interval(4, [1.0, 2.0, 3.0, 4.0]) == 3


def test_find_interval_errors():
    with pytest.raises(ValueError):
        find_interval(3.5, [1.0])
        find_interval(3.5, [1.0, 2.0, 4.0, 3.0])


def test_find_interval_property():
    a = find_interval(1.2, [1.0, 2.0, 3.0, 4.0])
    b = find_interval(6.2, [6.0, 7.0, 8.0, 9.0])
    assert a == b


def test_find_interval_random():
    my_intervals = list(np.random.rand(4))
    my_q = np.random.uniform(-100, 100)
    my_intervals.sort()
    a = find_interval(my_q, my_intervals)
    if -1 < a < 3:
        assert my_intervals[a] <= my_q < my_intervals[a+1]
    elif a >= 3:
        assert my_q >= my_intervals[a]
    else:
        assert my_q < my_intervals[a+1]
