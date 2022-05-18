from max_sum import *


def test_max_sub_array_sum():
    assert max_sub_array_sum([1, 2, 5, 2, 8, 1, 5], 2) == 10
    assert max_sub_array_sum([1, 2, 5, 2, 8, 1, 5], 4) == 17
    assert max_sub_array_sum([4, 2, 1, 6], 1) == 6
    assert max_sub_array_sum([4, 2, 1, 6, 2], 4) == 13
    assert max_sub_array_sum([], 4) is None


def test_max_sub_array_sum_naive():
    assert max_sub_array_sum_naive([1, 2, 5, 2, 8, 1, 5], 2) == 10
    assert max_sub_array_sum_naive([1, 2, 5, 2, 8, 1, 5], 4) == 17
    assert max_sub_array_sum_naive([4, 2, 1, 6], 1) == 6
    assert max_sub_array_sum_naive([4, 2, 1, 6, 2], 4) == 13
    assert max_sub_array_sum_naive([], 4) is None
