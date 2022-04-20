"""
Given a string, return true if the string is a palindrome
or false if it is not.

Palindromes are strings that form the same word if it is
reversed. *Do* include spaces and punctuation in determining
if the string is a palindrome.
"""


def palindrome(s: str) -> bool:
    return s == s[::-1]


def palindrome_optimized(s: str) -> bool:
    sl = len(s)
    half = sl // 2

    # use `for` loop to check if string is same on both sides
    # this is actually more efficient - O(N/2) - because we only
    # iterate over half the length of the string.
    for i in range(half):
        if s[i] != s[sl - 1 - i]:
            return False

    return True
