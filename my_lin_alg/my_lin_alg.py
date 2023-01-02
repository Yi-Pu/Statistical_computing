"""This file is to define the transpose fuction."""


def my_transpose(X):
    """This function is to transpose a matrix."""
    trans = [[0] * len(X) for i in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X[0])):
            trans[j][i] = X[i][j]
    return trans


def my_mat_prod(X, Y):
    """This function is to calculate the product of two matrix."""

    res = [[0] * len(Y[0]) for i in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                res[i][j] += X[i][k] * Y[k][j]
    return res
