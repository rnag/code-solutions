"""
Given a string consisting of small English letters, find and return the first
instance of a non-repeating character in it.

If there is no such character, return '_'.
"""

from __future__ import annotations

__all__ = ['first_non_repeating_character']

from collections import defaultdict


def first_non_repeating_character(string: str) -> str:
    n = len(string)

    if not n:
        return '_'

    if n == 1:
        return string

    freq = defaultdict(int)

    for c in string:
        freq[c] += 1

    return next((c for c, count in freq.items() if count == 1), '_')
