"""
Return the minimum number of minutes that must elapse until no cell has a
fresh orange. If this is impossible, return -1.


Links:
    - https://leetcode.com/problems/rotting-oranges/

"""
from __future__ import annotations

__all__ = ['rotting_oranges']


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

ROTTEN = 2
FRESH = 1
EMPTY = 0


def rotting_oranges(matrix: list[list[int]]) -> int:
    num_rows = len(matrix)
    if num_rows == 0:
        return 0
    num_cols = len(matrix[0])

    queue = []
    fresh_oranges = 0

    for r, row in enumerate(matrix):
        for c, col in enumerate(row):

            if col == ROTTEN:
                queue.append((r, c))

            elif col == FRESH:
                fresh_oranges += 1

    total_minutes = 0
    queue_size = len(queue)

    while queue:
        if queue_size == 0:
            queue_size = len(queue)
            total_minutes += 1

        r, c = queue.pop(0)
        queue_size -= 1

        for dr, dc in DIRECTIONS:
            next_row, next_col = r + dr, c + dc
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
                orange = matrix[next_row][next_col]
                if orange == FRESH:
                    matrix[next_row][next_col] = ROTTEN
                    fresh_oranges -= 1
                    queue.append((next_row, next_col))

    return -1 if fresh_oranges else total_minutes
