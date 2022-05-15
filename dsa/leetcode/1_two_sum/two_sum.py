"""
Given an `array` of integers nums and an integer `target`, return
indices of the two numbers such that they add up to `target`.

Links:
  - https://leetcode.com/problems/two-sum
  - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
from __future__ import annotations

__all__ = ['two_sum_naive',
           'two_sum',
           'two_sum_when_input_is_sorted']


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


def two_sum_when_input_is_sorted(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Optimized *two-pointer* approach for two-sum when input array is already sorted.

    Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

    Time complexity: O(N)
    Space complexity: O(1)
    """
    n = len(nums)
    if n < 2:
        return None

    # use a two-pointer approach, a `left` and `right` pointer at both ends
    l, r = 0, n - 1

    while l < r:
        sum2 = nums[l] + nums[r]

        if sum2 == target:  # we are done
            return l + 1, r + 1

        elif sum2 < target:
            l += 1

        else:  # sum > target
            r -= 1
