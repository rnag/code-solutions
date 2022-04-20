"""
Reverse a string in Python
"""


def reverse_idiomatic(s: str) -> str:
    return s[::-1]


def reverse(s: str) -> str:
    reversed_chars = [s[i] for i in range(len(s) - 1, -1, -1)]
    return ''.join(reversed_chars)


def reverse_v2(s: str) -> str:
    reversed_str = ''

    for c in s:
        reversed_str = c + reversed_str

    return reversed_str
