"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Links:
    - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

"""
from __future__ import annotations

__all__ = ['min_remove_to_make_valid']


def min_remove_to_make_valid(s: str) -> str:
    res = list(s)
    stack = []

    for i, c in enumerate(res):
        if c == '(':  # opening brace
            stack.append(i)

        elif c == ')':
            if stack:
                stack.pop()
            else:
                res[i] = ''

    while stack:
        curr_idx = stack.pop()
        res[curr_idx] = ''

    return ''.join(res)
