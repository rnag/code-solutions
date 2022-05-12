"""
Copy this template and create a new example file from it as needed

Links for reference:
    - https://leetcode.com/problems/knight-probability-in-chessboard/
"""

from __future__ import annotations

__all__ = ['knight_probability',
           'knight_probability_naive']


directions = [
    (-2, 1),
    (-2, -1),
    (-1, 2),
    (-1, -2),
    (1, 2),
    (1, -2),
    (2, 1),
    (2, -1)
]


def knight_probability_naive(n: int, k: int, r: int, c: int):
    if r < 0 or r >= n or c < 0 or c >= n:
        return 0

    if k == 0:
        return 1

    total = 0
    for x, y in directions:
        total += knight_probability_naive(n, k - 1, r + x, c + y)

    return total / 8


def knight_probability(n: int, k: int, r: int, c: int) -> float:
    """
    Solution using dynamic programming.

    TODO: Update as there might be a more optimal solution.
    """

    memo = {}

    def helper(x, y, k):

        if (x, y, k) in memo:
            return memo[(x, y, k)]

        if not (0 <= x < n and 0 <= y < n):
            return 0

        if k == 0:
            return 1

        total = 0
        for add_x, add_y in directions:
            total += helper(x + add_x, y + add_y, k - 1)

        memo[(x, y, k)] = total

        return total

    return helper(r, c, k) / 8 ** k
