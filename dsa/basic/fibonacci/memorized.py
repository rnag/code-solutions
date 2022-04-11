from timeit import timeit


def fib(n, memo=None):
    if memo is None:
        memo = {}
    elif n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = res = fib(n - 1, memo) + fib(n - 2, memo)

    return res


# 0.025 s
print('Recursive: ', timeit('fib(10)', globals=globals(), number=10000))

# 1.911 s
print('Recursive: ', timeit('fib(500)', globals=globals(), number=10000))
