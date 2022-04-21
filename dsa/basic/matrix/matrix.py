"""
Write a function that accepts an integer N
and returns a NxN spiral matrix.

--- Examples
  matrix(2)
    [[1, 2],
    [4, 3]]
  matrix(3)
    [[1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]
 matrix(4)
    [[1,   2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]]
"""
from __future__ import annotations


def matrix(n: int) -> list[list[int]]:
    # create empty matrix of NxN (all zeros)
    results = [[0] * n for _ in range(n)]
    # counter variable, should go from 1 ..= N^2
    counter = 1
    # start row and col, at 0
    start_row = start_col = 0
    # end row and col, at N - 1
    end_row = end_col = n - 1

    while start_row <= end_row and start_col <= end_col:
        # Top row

        for col in range(start_col, end_col + 1):
            results[start_row][col] = counter
            counter += 1
        # increment `start_row`, since we are done with this row
        start_row += 1

        # End column

        for row in range(start_row, end_row + 1):
            results[row][end_col] = counter
            counter += 1

        end_col -= 1

        # Bottom row

        for col in range(end_col, start_col - 1, -1):
            results[end_row][col] = counter
            counter += 1

        end_row -= 1

        # Start column

        for row in range(end_row, start_row - 1, -1):
            results[row][start_col] = counter
            counter += 1

        start_col += 1

    return results
