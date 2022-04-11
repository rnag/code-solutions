from timeit import timeit


def fib(n):
    memo = [0] * n
    memo[:3] = (0, 1, 1)

    for i in range(3, n):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n - 1] + memo[n - 2]


# 0.650 s
print('Iterative: ', timeit('fib(500)', globals=globals(), number=10000))
