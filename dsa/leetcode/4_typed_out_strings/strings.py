"""
Given two strings S and T, return if they are equal when they are both
typed out. Any '#' that appears in the string counts as a backspace.

Example:

>>> typed_out_strings('cb#d', 'cdz#')  # cd
True

Links:
    - https://leetcode.com/problems/backspace-string-compare/

"""
from __future__ import annotations

__all__ = ['typed_out_strings',
           'typed_out_strings_optimized',
           'typed_out_strings_optimized_better_space']


# Brute force solution
#
#   Time complexity: O(N+M)
#   Space complexity: O(N+M)
def typed_out_strings(s: str, t: str) -> bool:
    # note: technically this comparison is O(N)
    return build_string_arr(s) == build_string_arr(t)


def build_string_arr(s: str) -> list[str]:
    """Helper function for brute-force solution"""
    built_array = []
    n = 0  # keeps track of number of elements in array

    for char in s:
        if char == '#':
            if n:  # if built array is not empty
                n -= 1
                built_array.pop()  # remove last char
        else:
            n += 1
            built_array.append(char)

    return built_array


# Optimal solution using a more "idiomatic" Python approach
#
#  Time complexity: O(N+M)
#  Space complexity: O(N+M)
def typed_out_strings_optimized(s: str, t: str) -> bool:
    return process(s) == process(t)


def process(s: str) -> list[str]:
    result = []
    hash_skip = 0

    for char in reversed(s):
        if char == '#':
            hash_skip += 1
        elif hash_skip:
            hash_skip -= 1
        else:
            result.append(char)

    return result


# Optimal solution using a "Two Pointer" approach
#
#   Time complexity: O(N+M)
#   Space complexity: O(1)
def typed_out_strings_optimized_better_space(s: str, t: str) -> bool:
    p1, p2 = len(s) - 1, len(t) - 1

    while p1 >= 0 or p2 >= 0:
        c1 = s[p1] if p1 >= 0 else None
        c2 = t[p2] if p2 >= 0 else None

        if c1 == '#' or c2 == '#':

            if c1 == '#':
                p1 = backspace(s, p1)

            if c2 == '#':
                p2 = backspace(t, p2)

        else:
            if c1 != c2:
                return False

            p1 -= 1
            p2 -= 1

    return True


def backspace(s: str, idx: int) -> int:
    back_count = 2
    while back_count > 0:
        idx -= 1
        if idx < 0:
            break
        back_count -= 1
        if s[idx] == '#':
            back_count += 2

    return idx
