"""Implement find_interval."""


def find_interval(query_point, intervals):
    """Find the index of the largest endpoint that is <= query_point.

    If query_point lies below all the endpoints, return one less than the
    minimum index.

    Parameters:

    query_point: number to test
    intervals: ordered list of numbers defining the intervals

    Output: index of the endpoint
    """

    if len(intervals) == 0:
        raise ValueError("At least one interval endpoint must be provided")

    for i in range(len(intervals)-1):
        if intervals[i] >= intervals[i+1]:
            raise ValueError("Condition (1) violated")

    for idx, endpoint in enumerate(intervals):
        if query_point < endpoint:
            return idx - 1

    return len(intervals) - 1
