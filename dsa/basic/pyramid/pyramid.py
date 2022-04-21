"""
Write a function that accepts a positive number N.
The function should console log a pyramid shape
with N levels using the # character.  Make sure the
pyramid has spaces on both the left *and* right hand sides
--- Examples
  pyramid(1)
      '#'
  pyramid(2)
      ' # '
      '###'
  pyramid(3)
      '  #  '
      ' ### '
      '#####'

"""


def pyramid_idiomatic(n: int, fill='#') -> None:
    # the base width of triangle (bottom)
    base_width = n * 2 - 1

    for i in range(1, n + 1):
        print(repr(f'{fill * (i * 2 - 1):^{base_width}}'))


def pyramid(n: int) -> None:
    # the base width of triangle (bottom)
    base_width = n * 2 - 1
    # midpoint of triangle (roughly)
    mid = base_width // 2

    for row in range(n):
        # if current `col` index is within midpoint += `row` index, then
        # use the "#" character
        level = ''.join('#' if mid - row <= col <= mid + row else ' '
                        for col in range(base_width))

        print(repr(level))
