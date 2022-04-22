

def memoize(fn):
    """Generic decorator to memorize the result of a function `fn`"""
    cache = {}

    def new_fn(*args):
        if args in cache:
            return cache[args]
        result = cache[args] = fn(*args)
        return result

    return new_fn


def slow_fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


# memorize the `slow_fib` function
fib = memoize(slow_fib)


if __name__ == '__main__':
    from timeit import timeit

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(39) == 63245986

    # 0.002 s
    print('Recursive: ', timeit('fib(10)', globals=globals(), number=10000))

    # 0.003 s
    print('Recursive: ', timeit('fib(500)', globals=globals(), number=10000))
