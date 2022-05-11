from min_cost import *


def test_min_cost_climbing_stairs():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_min_cost_climbing_stairs_bottom_up():
    assert min_cost_climbing_stairs_bottom_up([10, 15, 20]) == 15
    assert min_cost_climbing_stairs_bottom_up([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
