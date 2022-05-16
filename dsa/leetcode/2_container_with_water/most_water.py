"""
Copy this template and create a new example file from it as needed

Links:
    - https://leetcode.com/problems/container-with-most-water/
    - https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms
"""
from __future__ import annotations

__all__ = ['container_with_most_water',
           'container_with_most_water_optimized']


# Brute force solution
#
#   Time complexity: O(N^2)
#   Space complexity: O(1)
def container_with_most_water(heights: list[int]) -> int:
    n = len(heights)
    max_area = 0

    for a in range(n):
        for b in range(a + 1, n):
            height = min(heights[a], heights[b])
            width = b - a
            area = height * width
            max_area = max(max_area, area)
            # alternatively:
            #   if area > max_area:
            #       max_area = area

    return max_area


# Optimal solution using a "Two Pointer" approach
#
#   Time complexity: O(N)
#   Space complexity: O(1)
def container_with_most_water_optimized(heights: list[int]) -> int:
    max_area = 0
    # use a two-pointer approach, a `left` and `right` pointer at both ends
    l, r = 0, len(heights) - 1

    while l < r:
        h_left, h_right = heights[l], heights[r]

        height = min(h_left, h_right)
        width = r - l
        area = height * width

        # alternatively:
        #  if area > max_area:
        #      max_area = area
        max_area = max(max_area, area)

        if h_left <= h_right:
            l += 1
        else:
            r -= 1

    return max_area
