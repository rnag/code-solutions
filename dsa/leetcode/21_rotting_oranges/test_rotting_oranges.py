from rotting_oranges import *


def test_rotting_oranges():
    assert rotting_oranges(
        [
            [2, 1, 1, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1]
        ]
    ) == 7

    assert rotting_oranges(
        [
            [1, 1, 0, 0, 0],
            [2, 1, 0, 0, 0],
            [0, 0, 0, 1, 2],
            [0, 1, 0, 0, 1]
        ]
    ) == -1

    assert rotting_oranges([]) == 0
    assert rotting_oranges([
        [],
        []
    ]) == 0
