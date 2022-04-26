from rainwater import *


def test_trapping_rainwater():
    # zeros
    assert trapping_rainwater([]) == 0
    assert trapping_rainwater([7]) == 0
    assert trapping_rainwater([7, 3]) == 0
    assert trapping_rainwater([3, 4, 3]) == 0

    assert trapping_rainwater([4, 2, 0, 3, 2, 5]) == 9
    assert trapping_rainwater(
        [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
    assert trapping_rainwater(
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_trapping_rainwater_optimized():
    # zeros
    assert trapping_rainwater_optimized([]) == 0
    assert trapping_rainwater_optimized([7]) == 0
    assert trapping_rainwater_optimized([7, 3]) == 0
    assert trapping_rainwater_optimized([3, 4, 3]) == 0

    assert trapping_rainwater_optimized([4, 2, 0, 3, 2, 5]) == 9
    assert trapping_rainwater_optimized(
        [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
    assert trapping_rainwater_optimized(
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
