from time_to_inform_employees import *


def test_time_needed_to_inform_employees():
    assert time_needed_to_inform_employees(1, 0, [-1], [0]) == 0
    assert time_needed_to_inform_employees(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1
