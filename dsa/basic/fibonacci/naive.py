from timeit import timeit


def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


# NOTE: the below times only for N=10
#
# Meaning, the time complexity is BEYOND TERRIBLE!
#
# 0.102 s
print('Naive: ', timeit('fib(10)', globals=globals(), number=10000))
