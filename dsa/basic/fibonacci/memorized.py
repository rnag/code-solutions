

def fib(n, memo=None):
    """
    Recursive implementation using a dictionary object to store the previous
    results of calling `fib`.

    Time complexity: O(N)
    Space complexity: O(2 * N)
        - Notes: the Space complexity of a recursive function call is O(N) alone.
    """
    if memo is None:
        # initialize `memo` object
        memo = {}
    elif n in memo:
        # check if `fib(n)` was already calculated
        return memo[n]

    if n <= 1:
        return n

    memo[n] = res = fib(n - 1, memo) + fib(n - 2, memo)

    return res


if __name__ == '__main__':
    from timeit import timeit

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(39) == 63245986

    # 0.025 s
    print('Recursive: ', timeit('fib(10)', globals=globals(), number=10000))

    # 1.911 s
    print('Recursive: ', timeit('fib(500)', globals=globals(), number=10000))
