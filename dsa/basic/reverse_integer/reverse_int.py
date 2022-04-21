"""
Given an integer, return an integer that is the reverse
ordering of numbers.

--- Examples
  reverse_int(15) === 51
  reverse_int(981) === 189
  reverse_int(500) === 5
  reverse_int(-15) === -51
  reverse_int(-90) === -9
"""


def reverse_int(n: int) -> int:
    if n < 0:   # is the number negative? i.e. `-2`
        reversed_str = '-' + str(n)[:0:-1]
    else:
        reversed_str = str(n)[::-1]

    return int(reversed_str)


def reverse_int_optimized(n: int) -> int:
    rev_number = 0
    is_negative = n < 0

    if is_negative:
        n = -n

    while n > 0:
        rem = n % 10
        rev_number = rev_number * 10 + rem
        n //= 10

    return -rev_number if is_negative else rev_number
