"""
Write a program that console logs the numbers
from 1 to n. But for multiples of three print
“fizz” instead of the number and for the multiples
of five print “buzz”. For numbers which are multiples
of both three and five print “fizzbuzz”.

--- Example
  fizz_buzz(5);
  1
  2
  fizz
  4
  buzz

"""


def fizz_buzz(n: int) -> None:
    for i in range(1, n + 1):
        if not i % 15:  # is `n` is a multiple of 15?
            print('fizzbuzz')
        elif not i % 3:  # is `n` is a multiple of 3?
            print('fizz')
        elif not i % 5:  # is `n` is a multiple of 5?
            print('buzz')
        else:
            print(i)
