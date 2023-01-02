# This script is to test if the sort methods work correctly
import pytest
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from selection_sort import selection_sort
from quick_sort import quick_sort, improved_quick_sort
from numpy import random
import numpy as np


# This creates a "test fixture". This is an easy way to create data that's
# needed by your tests, and if one test changes the data in some way, the
# other tests get a clean untouched copy.
@pytest.fixture
def example_list():
    # Ordinary list
    ls1 = [1, 3, 5, 1, -1, 7, 8, 9]
    ls2 = [2, 9, 0, 2, -1, 9]
    # Random list
    ls3 = list(random.normal(0, 1, size=5))

    return [ls1, ls2, ls3]


def test_bubble_sort(example_list):
    # ls1_bubble = bubble_sort(example_list[0])
    # ls2_bubble = bubble_sort(example_list[1])
    # ls3_bubble = bubble_sort(example_list[2])
    # ls1_numpy = np.sort(example_list[0])
    # ls2_numpy = np.sort(example_list[1])
    # ls3_numpy = np.sort(example_list[2])
    # assert ls1_bubble.all() == ls1_numpy.all()
    # assert ls2_bubble.all() == ls2_numpy.all()
    # assert ls3_bubble.all() == ls3_numpy.all()
    assert (
        bubble_sort(example_list[0]) ==
        np.sort(example_list[0])).all()
    assert (
        bubble_sort(example_list[1]) ==
        np.sort(example_list[1])).all()
    assert (
        bubble_sort(example_list[2]) ==
        np.sort(example_list[2])).all()


def test_merge_sort(example_list):
    assert (
        merge_sort(example_list[0]) ==
        np.sort(example_list[0])).all()
    assert (
        merge_sort(example_list[1]) ==
        np.sort(example_list[1])).all()
    assert (
        merge_sort(example_list[2]) ==
        np.sort(example_list[2])).all()


def test_selection_sort(example_list):
    assert (
        selection_sort(example_list[0]) ==
        np.sort(example_list[0])).all()
    assert (
        selection_sort(example_list[1]) ==
        np.sort(example_list[1])).all()
    assert (
        selection_sort(example_list[2]) ==
        np.sort(example_list[2])).all()


def test_quick_sort(example_list):
    assert (
        quick_sort(example_list[0], 0, 7) ==
        np.sort(example_list[0])).all()
    assert (
        quick_sort(example_list[1], 0, 5) ==
        np.sort(example_list[1])).all()
    assert (
        quick_sort(example_list[2], 0, 4) ==
        np.sort(example_list[2])).all()


def test_improved_quick_sort(example_list):
    assert (
        improved_quick_sort(example_list[0], 0, 7) ==
        np.sort(example_list[0])).all()
    assert (
        improved_quick_sort(example_list[1], 0, 5) ==
        np.sort(example_list[1])).all()
    assert (
        improved_quick_sort(example_list[2], 0, 4) ==
        np.sort(example_list[2])).all()
