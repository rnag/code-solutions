"""
Find the minimum cost of climbing stairs

Links for reference:
    - https://leetcode.com/problems/min-cost-climbing-stairs/
    - https://youtu.be/ktmzAZWkEZ0
"""

from __future__ import annotations

__all__ = ['min_cost_climbing_stairs']


def min_cost_climbing_stairs(cost: list[int]) -> int:
    cost.append(0)

    for i in range(len(cost) - 3, -1, -1):
        cost_to_add = min(cost[i + 1], cost[i + 2])
        cost[i] += cost_to_add

    return min(cost[0], cost[1])
