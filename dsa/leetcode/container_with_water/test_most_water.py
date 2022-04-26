from most_water import *


def test_container_with_most_water():
    # zero's
    assert container_with_most_water([]) == 0
    assert container_with_most_water([7]) == 0
    # the 8 and 9 provides the max area -> min(8, 9) * (4 - 1) = 24
    assert container_with_most_water([1, 8, 6, 2, 9, 4]) == 24
    # the 7 and 3 provides the max area -> min(7, 3) * (5 - 1) = 12
    assert container_with_most_water([1, 7, 2, 0, 1, 3]) == 12
    # the 7 and 9 provides the max area -> min(7, 9) * (4 - 0) = 28
    assert container_with_most_water([7, 1, 2, 3, 9]) == 28
    # the 7 and 9 provides the max area -> min(7, 9) * (3 - 2) = 7
    assert container_with_most_water([1, 3, 7, 9, 2]) == 7


def test_container_with_most_water_optimized():
    assert container_with_most_water_optimized([]) == 0
    assert container_with_most_water_optimized([7]) == 0
    assert container_with_most_water_optimized([1, 8, 6, 2, 9, 4]) == 24
    assert container_with_most_water_optimized([1, 7, 2, 0, 1, 3]) == 12
    assert container_with_most_water_optimized([7, 1, 2, 3, 9]) == 28
    assert container_with_most_water_optimized([1, 3, 7, 9, 2]) == 7
