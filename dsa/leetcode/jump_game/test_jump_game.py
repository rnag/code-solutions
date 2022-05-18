from jump_game import *


def test_can_jump():
    assert can_jump([1, 2, 0, 1])
    assert can_jump([3, 0, 8, 2, 0, 0, 1])
    assert can_jump([2, 3, 1, 1, 4])
    assert not can_jump([3, 2, 1, 0, 4])
    assert can_jump([1, 2])


def test_can_jump_iterative():
    assert can_jump_iterative([1, 2, 0, 1])
    assert can_jump_iterative([3, 0, 8, 2, 0, 0, 1])
    assert can_jump_iterative([2, 3, 1, 1, 4])
    assert not can_jump_iterative([3, 2, 1, 0, 4])
    assert can_jump_iterative([1, 2])
