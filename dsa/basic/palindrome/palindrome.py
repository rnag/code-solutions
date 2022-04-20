"""
Given a string, return true if the string is a palindrome
or false if it is not.

Palindromes are strings that form the same word if it is
reversed. *Do* include spaces and punctuation in determining
if the string is a palindrome.
"""


def palindrome(s: str) -> bool:
    return s == s[::-1]
