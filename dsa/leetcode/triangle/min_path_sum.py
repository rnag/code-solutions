"""
Given a triangle array, return the minimum path sum from top to bottom.

Links for reference:
    - https://leetcode.com/problems/triangle
    - https://youtu.be/OM1MTokvxs4
"""

from __future__ import annotations

__all__ = ['minimum_path_sum',
           'minimum_path_sum_optimized']


def minimum_path_sum(triangle: list[list[int]]) -> int:
    dp = [0] * (len(triangle) + 1)

    for row in triangle[::-1]:
        for i, n in enumerate(row):
            dp[i] = n + min(dp[i], dp[i + 1])

    return dp[0]


def minimum_path_sum_optimized(triangle: list[list[int]]) -> int:
    dp = triangle.pop()
    dp.append(0)

    for row in reversed(triangle):
        for i, n in enumerate(row):
            dp[i] = n + min(dp[i], dp[i + 1])

    return dp[0]


