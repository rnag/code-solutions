"""
Given an array of integers representing an elevation map where the
width of each bar is 1, return how much rainwater can be trapped.

"""
from __future__ import annotations

__all__ = ['trapping_rainwater',
           'typed_out_strings_optimized']


# Brute force solution
#
# Time complexity: O(N^2)
def trapping_rainwater(heights: list[int]) -> int:
    total_water = 0
    try:
        max_left = heights[0]
    except IndexError:
        return total_water

    for i in range(1, len(heights) - 1):
        current_height = heights[i]
        max_right = max(heights[i+1:])
        water = min(max_left, max_right) - current_height

        if water > 0:
            total_water += water

        if current_height > max_left:
            max_left = current_height

    return total_water


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
# Time complexity: O(N)
def typed_out_strings_optimized(s: str, t: str) -> bool:
    return process(s) == process(t)
