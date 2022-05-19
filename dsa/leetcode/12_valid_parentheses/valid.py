"""
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

Links:
    - https://leetcode.com/problems/valid-parentheses/

"""
from __future__ import annotations

__all__ = ['is_valid_parentheses']


def is_valid_parentheses(s: str) -> bool:

    if not s:  # an empty string is valid
        return True

    # mapping of `open` to `close` brackets
    parens = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    stack = []

    for c in s:

        if c in parens:  # opening brace
            stack.append(c)

        else:  # closing brace
            if not stack:
                return False

            left_bracket = stack.pop()
            correct_bracket = parens[left_bracket]

            if correct_bracket != c:
                return False

    # check for any remaining open brackets - ex. '({[]'
    return len(stack) == 0
