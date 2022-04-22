

def fib(n):
    """
    This is uses a tabulated, "bottom-up" approach which is quite efficient.

    The idea is to start from the start, and build up the list as we go all the
    way up to `n - 1`.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    memo = [0] * n
    memo[:3] = (0, 1, 1)

    if n < 3:
        return memo[n]

    for i in range(3, n):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n - 1] + memo[n - 2]


if __name__ == '__main__':
    from timeit import timeit

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(39) == 63245986

    # 0.010 s
    print('Iterative: ', timeit('fib(10)', globals=globals(), number=10000))

    # 0.650 s
    print('Iterative: ', timeit('fib(500)', globals=globals(), number=10000))
