from basic.palindrome.palindrome import palindrome, palindrome_optimized
from basic.reverse_integer.reverse_int import reverse_int, reverse_int_optimized


def test_compare_times():
    from timeit import timeit
    n = 1_000_000

    print('reverse_int_optimized: ', timeit("reverse_int_optimized(981)", globals=globals(), number=n))
    print('reverse_int:           ', timeit("reverse_int(981)", globals=globals(), number=n))


def test_reverse_int():
    assert reverse_int(15) == 51
    assert reverse_int(981) == 189
    assert reverse_int(500) == 5
    assert reverse_int(-15) == -51
    assert reverse_int(-90) == -9


def test_reverse_int_optimized():
    assert reverse_int_optimized(15) == 51
    assert reverse_int_optimized(981) == 189
    assert reverse_int_optimized(500) == 5
    assert reverse_int_optimized(-15) == -51
    assert reverse_int_optimized(-90) == -9
