from count_unique_values import *


def test_count_unique_values_single_ptr():
    assert count_unique_values_single_ptr([1, 1, 1, 1, 2]) == 2
    assert count_unique_values_single_ptr([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]) == 7
    assert count_unique_values_single_ptr([]) == 0
    assert count_unique_values_single_ptr([7]) == 1
    assert count_unique_values_single_ptr([-2, -1, -1, 0, 1]) == 4


def test_count_unique_values():
    assert count_unique_values([1, 1, 1, 1, 2]) == 2
    assert count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]) == 7
    assert count_unique_values([]) == 0
    assert count_unique_values([7]) == 1
    assert count_unique_values([-2, -1, -1, 0, 1]) == 4


def test_compare_times():
    from timeit import timeit

    n = 100_000

    # 0.034
    print(f'count_unique_values_single_ptr:  '
          f'{timeit("count_unique_values_single_ptr([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])", globals=globals(), number=n):.3f}')
    # 0.068
    print(f'count_unique_values:             '
          f'{timeit("count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13])", globals=globals(), number=n):.3f}')
