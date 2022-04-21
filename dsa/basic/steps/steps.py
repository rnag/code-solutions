"""
Write a function that accepts a positive number N.
The function should console log a step shape
with N levels using the # character.  Make sure the
step has spaces on the right hand side!
--- Examples
  steps(2)
      '# '
      '##'
  steps(3)
      '#  '
      '## '
      '###'
  steps(4)
      '#   '
      '##  '
      '### '
      '####'
"""


def steps_idiomatic(n: int, fill='#') -> None:
    for i in range(1, n + 1):
        print(repr(f'{fill * i:{n}}'))


def steps(n: int) -> None:
    for row in range(n):
        step = ''.join('#' if col <= row else ' ' for col in range(n))
        print(repr(step))
