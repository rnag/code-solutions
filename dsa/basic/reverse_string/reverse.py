"""
Reverse a string in Python
"""


def reverse(s: str) -> str:
    reversed_chars = [s[i] for i in range(len(s) - 1, -1, -1)]
    return ''.join(reversed_chars)


def reverse_idiomatic(s: str) -> str:
    return s[::-1]
