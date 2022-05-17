"""
Given a string `s`, find the length of the longest substring without
repeating characters.

Links:
    - https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
from __future__ import annotations

__all__ = ['longest_substring',
           'longest_substring_optimized']


def longest_substring(s: str) -> int:
    """
    Brute-force solution

    Time complexity: O(N^2)
    Space complexity: O(N)
    """
    n = len(s)
    if n <= 1:
        return n

    longest = 0

    for left in range(n):
        seen = {s[left]}
        count = 1

        for right in range(left + 1, n):
            c = s[right]
            if c not in seen:
                seen.add(c)
                count += 1
            else:
                break

        longest = max(longest, count)

    return longest


def longest_substring_optimized(s: str) -> int:
    """
    Optimized solution using sliding-window technique.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    longest = count = l = 0
    seen = {}

    for r, char in enumerate(s):
        seen_index = seen.get(char, -1)

        if seen_index >= l:
            longest = max(longest, count)
            l = seen_index + 1
            count = r - l + 1
        else:
            count += 1

        seen[char] = r

    longest = max(longest, count)

    return longest
