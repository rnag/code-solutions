"""
Given an `array` of integers nums and an integer `target`, return
indices of the two numbers such that they add up to `target`.

"""
from __future__ import annotations

__all__ = ['two_sum_naive',
           'two_sum']


def two_sum_naive(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Naive approach for two-sum.

    Time complexity: O(N^2)
    Space complexity: O(1)
    """
    length = len(nums)

    if length < 2:
        return None

    for i in range(length):
        num_to_find = target - nums[i]
        for j in range(i + 1, length):
            if num_to_find == nums[j]:
                return i, j

    return None


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Optimized approach for two-sum.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    # cache containing the number to find (other pair) to first pair's index
    #   ex. {num_to_find: index}
    nums_cache = {}

    for i, n in enumerate(nums):
        if n in nums_cache:
            return nums_cache[n], i

        num_to_find = target - n
        nums_cache[num_to_find] = i

    return None
