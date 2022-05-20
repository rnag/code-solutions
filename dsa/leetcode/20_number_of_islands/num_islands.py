"""
Given an m x n 2D binary grid `grid` which represents a map of '1's (land)
and '0's (water), return the number of islands.

Links:
    - https://leetcode.com/problems/number-of-islands/
"""
from __future__ import annotations

from collections import deque

__all__ = ['num_islands']


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def num_islands(matrix: list[list[int]]) -> int:
    island_count = 0

    nr = len(matrix)
    if nr == 0:
        return 0

    nc = len(matrix[0])

    for row in range(nr):
        for col in range(nc):
            if matrix[row][col] == 1:
                island_count += 1
                matrix[row][col] = 0

                queue = deque()
                queue.append((row, col))

                while queue:
                    r, c = queue.popleft()

                    for x, y in DIRECTIONS:
                        next_row, next_col = r + x, c + y

                        if 0 <= next_row < nr and 0 <= next_col < nc:
                            if matrix[next_row][next_col] == 1:
                                queue.append((next_row, next_col))
                                matrix[next_row][next_col] = 0

    return island_count
