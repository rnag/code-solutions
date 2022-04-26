"""
Given an array of integers representing an elevation map where the
width of each bar is 1, return how much rainwater can be trapped.

"""
from __future__ import annotations

__all__ = ['trapping_rainwater',
           'trapping_rainwater_optimized']


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


# Optimal solution using a "Two Pointer" approach
#
# Time complexity: O(N)
def trapping_rainwater_optimized(heights: list[int]) -> int:
    ln = len(heights)

    if not ln:  # heights is empty
        return 0

    left = 0
    right = ln - 1

    max_left = heights[left]
    max_right = heights[right]

    total_water = 0

    while left < right:
        if max_left <= max_right:
            left += 1

            height = heights[left]
            if height >= max_left:
                max_left = height
            else:
                water = max_left - height
                total_water += water
        else:
            right -= 1

            height = heights[right]
            if height >= max_right:
                max_right = height
            else:
                water = max_right - height
                total_water += water

    return total_water
