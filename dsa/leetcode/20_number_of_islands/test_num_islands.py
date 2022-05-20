from num_islands import *


def test_num_islands():
    assert num_islands(
        [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 1, 1]
        ]
    ) == 2

    assert num_islands([
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]) == 1

    assert num_islands(
        [
            [0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1]
        ]
    ) == 7
