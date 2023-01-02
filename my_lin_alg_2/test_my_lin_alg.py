# Implement your unit tests in this file


from my_lin_alg import my_transpose, my_mat_prod
import numpy as np
import pytest

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
# 3x3 matrix
Z = np.array(
    [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]])


def test_my_transpose():
    assert (my_transpose(X) == np.transpose(X)).all()


def test_my_mat_prod():
    assert (my_mat_prod(X, Y) == np.dot(X, Y)).all()


def test_my_mat_prod_invalid_values():
    with pytest.raises(ValueError):
        my_mat_prod(Y, X)


def test_properties():
    K = my_transpose(my_transpose(X))
    assert (X == K).all()
    J = my_transpose(np.dot(X, 3))
    Q = np.dot(my_transpose(X), 3)
    assert (J == Q).all()
    N = my_mat_prod(np.dot(X, 3), Y)
    P = np.dot(my_mat_prod(X, Y), 3)
    assert (N == P).all()
    M = my_mat_prod(X, Z)
    assert (X == M).all()


def test_random():
    A = np.random.rand(5, 3)
    assert (my_transpose(A) == np.transpose(A)).all()


def test_edge():
    D = np.random.rand(1, 1)
    C = np.random.rand(1, 1)
    assert (my_transpose(C) == np.transpose(C)).all()
    assert (my_mat_prod(D, C) == np.dot(D, C)).all()


def test_error():
    D = np.random.rand(0, 0)
    C = np.random.rand(0, 0)
    try:
        my_mat_prod(C, D)
    except IndexError as err:
        print("Exception: " + str(err))
