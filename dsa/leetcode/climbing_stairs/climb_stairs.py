"""
Find the minimum cost of climbing stairs

Links for reference:
    - https://leetcode.com/problems/climbing-stairs/
    - https://youtu.be/Y0lT9Fck7qI
"""

from __future__ import annotations

__all__ = ['climbing_stairs']


def climbing_stairs(n: int) -> int:
    one = two = 1

    for _ in range(n - 1):
        one, two = one + two, one

    return one
