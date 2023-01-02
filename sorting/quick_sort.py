# This script is to implement quick sort
from numpy import random


# function to perform partition
def partition(A, p, r):

    # Pick the last element of the array as the pivot
    x = A[r]

    # pointer for greater element
    i = p - 1

    # traverse through all elements
    # and compare each element with pivot
    for j in range(p, r):

        # If element smaller than pivot is found
        # swap it with the greater element pointed by i
        if A[j] <= x:
            i = i + 1
            # Swap a_i and a_j
            (A[i], A[j]) = (A[j], A[i])

    # Swap the pivot element with the greater element specified by i
    (A[i + 1], A[r]) = (A[r], A[i + 1])

    return i + 1


# function to perform quicksort
def quick_sort(A, p, r):

    if p < r:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        q = partition(A, p, r)

        # Recursive call on the left of pivot
        quick_sort(A, p, q-1)

        # Recursive call on the right of pivot
        quick_sort(A, q+1, r)

    return A


# function to perform improved partition
def improved_partition(A, p, r):

    # Pick a random element as the pivot
    pivot = random.randint(p, r)

    (A[r], A[pivot]) = (A[pivot], A[r])
    return partition(A, p, r)


# function to perform improved quicksort
def improved_quick_sort(A, p, r):

    if p < r:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        q = improved_partition(A, p, r)

        # Recursive call on the left of pivot
        improved_quick_sort(A, p, q-1)

        # Recursive call on the right of pivot
        improved_quick_sort(A, q+1, r)

        return A
