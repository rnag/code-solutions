"""
Print out the n-th entry in the fibonacci series.
The fibonacci series is an ordering of numbers where
each number is the sum of the preceding two.

For example, the sequence
 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
forms the first ten entries of the fibonacci series.

Example:
  fib(4) === 3
"""


# Notes: runtime is exponential (2 ^ N) because for every increase
# in a number N, we are going to get a dramatic increase in the
# number of function calls.
def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    from timeit import timeit

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    # commented out because it takes too long to run xD
    # assert fib(39) == 63245986

    # NOTE: the below times only for N=10
    #
    # Meaning, the time complexity is BEYOND TERRIBLE!
    #
    # 0.102 s
    print('Naive: ', timeit('fib(10)', globals=globals(), number=10000))
