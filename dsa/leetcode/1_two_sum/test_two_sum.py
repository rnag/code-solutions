from two_sum import *


def test_two_sum_naive():
    assert two_sum_naive([], 3) is None
    assert two_sum_naive([5], 1) is None

    nums_array = [1, 3, 7, 9, 2]
    target_to_find = 11

    assert two_sum_naive(nums_array, target_to_find) == (3, 4)


def test_two_sum():
    assert two_sum([], 3) is None
    assert two_sum([5], 1) is None

    nums_array = [1, 3, 7, 9, 2]
    target_to_find = 11

    assert two_sum(nums_array, target_to_find) == (3, 4)
