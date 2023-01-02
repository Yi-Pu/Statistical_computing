# This is to test is the croeded_cows fuction works correctly
from crowded_cows import crowded_cows
import pytest


def test_regular_values():
    assert crowded_cows([7, 3, 4, 2, 3, 4], 3)\
        == 4
    assert crowded_cows([7, 3, 4, 2, 3, 10, 4], 3)\
        == 3
    assert crowded_cows([7, 3, 1, 0, 4, 2, 16, 28, 3, 4], 3)\
        == -1


def test_errors():
    with pytest.raises(ValueError):
        crowded_cows([7, 3, 4, 2, 3, 4], 0.5)
        crowded_cows([], 0.5)


def test_edge_values():
    assert crowded_cows([7], 1) == -1
    assert crowded_cows([7, 3, 4, 2, 3, 4, 7], 100000) == 7
