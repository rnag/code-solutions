from min_path_sum import *


def test_minimum_path_sum():
    assert minimum_path_sum([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert minimum_path_sum([[-10]]) == -10


def test_minimum_path_sum_optimized():
    assert minimum_path_sum_optimized([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert minimum_path_sum_optimized([[-10]]) == -10
