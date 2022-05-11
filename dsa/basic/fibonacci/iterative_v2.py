

def fib(n):
    """
    This is uses a tabulated, "bottom-up" approach which is quite efficient.

    The idea is to start from the start, and only calculate two numbers at a
    time rather than building up a list, to save a bit more on space complexity.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    if n < 2:
        return n

    a, b = 1, 2

    for _ in range(n - 2):
        a, b = b, a + b

    return a


if __name__ == '__main__':
    from timeit import timeit

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(39) == 63245986

    # 0.005 s
    print('Iterative: ', timeit('fib(10)', globals=globals(), number=10000))

    # 0.225 s
    print('Iterative: ', timeit('fib(500)', globals=globals(), number=10000))
