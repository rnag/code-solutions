"""
Copy this template and create a new example file from it as needed

Links:
    - https://leetcode.com/problems/generate-parentheses/
    - https://youtu.be/s9fokUqJ76A
    -

"""
from __future__ import annotations

__all__ = ['generate_parentheses']


def generate_parentheses(n: int) -> list[str]:
    # only add an open parenthesis if `open < n`
    # only add a close parenthesis if `closed < open`
    #
    # we are done when open = close = n

    stack = []
    res = []

    def backtrack(open_n: int, closed_n: int):
        if open_n == closed_n == n:
            res.append(''.join(stack))
            return

        if open_n < n:
            stack.append('(')
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(')')
            backtrack(open_n, closed_n + 1)
            stack.pop()

    backtrack(0, 0)

    return res
