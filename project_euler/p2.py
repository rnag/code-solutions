"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def solution():
    print(fib_even_sum())


def fib_even_sum(c_sum=0, n0=0, n1=2, max=4_000_000):
    c_sum += n1

    # print('BEFORE: ', n0, n1)
    n1, n0 = n1 * 4 + n0, n1
    # print('AFTER:  ', n0, n1)
    # print()

    if n1 < max:
        # print(n0)
        return fib_even_sum(c_sum, n0, n1, max)
    else:
        return c_sum


"""note: unused :-)

def fib(n):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)
"""


if __name__ == '__main__':
    solution()
