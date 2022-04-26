"""
Copy this template and create a new example file from it as needed

"""
from __future__ import annotations

__all__ = ['container_with_most_water',
           'container_with_most_water_optimized']


# Brute force solution
#
# Time complexity: O(N^2)
def container_with_most_water(heights: list[int]) -> int:
    ln = len(heights)
    max_area = 0

    for i in range(ln):
        for j in range(i + 1, ln):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width
            if area > max_area:
                max_area = area

    return max_area


# Optimal solution using a "Two Pointer" approach
#
# Time complexity: O(N)
def container_with_most_water_optimized(heights: list[int]) -> int:
    max_area = 0

    p1 = 0
    p2 = len(heights) - 1

    while p1 < p2:
        elem_p1, elem_p2 = heights[p1], heights[p2]

        height = min(elem_p1, elem_p2)
        width = p2 - p1
        area = height * width

        # alternatively:
        #  if area > max_area:
        #      max_area = area
        max_area = max(max_area, area)

        if elem_p1 <= elem_p2:
            p1 += 1
        else:
            p2 -= 1

    return max_area
