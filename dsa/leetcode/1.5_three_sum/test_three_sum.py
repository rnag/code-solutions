from three_sum import *


def test_two_sum_naive():
    assert three_sum_naive([]) == []
    assert three_sum_naive([5]) == []
    assert three_sum_naive([5, 2]) == []
    assert three_sum_naive([1, 3, 7, 9, 2]) == []
    # expected failure (has duplicates)
    assert three_sum_naive([-1, 0, 1, 2, -1, -4]) == [(-1, -1, 2), (-1, 0, 1)]


def test_three_sum():
    assert three_sum([]) == []
    assert three_sum([5]) == []
    assert three_sum([5, 2]) == []
    assert three_sum([1, 3, 7, 9, 2]) == []
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [(-1, -1, 2), (-1, 0, 1)]
