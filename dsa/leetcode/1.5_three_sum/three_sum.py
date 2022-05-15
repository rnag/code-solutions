"""
Given an integer array nums, return all the triplets
`[nums[i], nums[j], nums[k]]` such that i != j, i != k, and j != k,
and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Links:
    https://leetcode.com/problems/3sum/
"""
from __future__ import annotations

__all__ = ['three_sum_naive',
           'three_sum']


def three_sum_naive(nums: list[int]) -> list[tuple[int, int, int]]:
    """
    Naive approach for three-sum.

    Time complexity: O(N^3)
    Space complexity: O(N)
    """
    length = len(nums)
    res = []

    if length < 3:
        return res

    for i in range(length):
        n = nums[i]
        target = -n
        for j in range(i + 1, length):
            # note: this now becomes a `two sum` problem
            num_to_find = target - nums[j]
            for k in range(j + 1, length):
                if num_to_find == nums[k]:
                    res.append((n, nums[j], nums[k]))

    return res


def three_sum(nums: list[int]) -> list[tuple[int, int, int]]:
    """
    Optimized approach for three-sum.

    Time complexity: O(N^2)
    Space complexity: O(N)
    """

    # sort the given array - O(N * log(N))
    nums.sort()

    length, prev_num, result = len(nums), None, []

    for i in range(length):
        n = nums[i]

        if n == prev_num:
            continue  # skip duplicates

        prev_num = n

        # convert 3sum to 2sum problem

        target = -n

        left, right = i + 1, length - 1

        while left < right:
            n_left, n_right = nums[left], nums[right]

            sum2 = n_left + n_right

            if sum2 == target:
                result.append((n, n_left, n_right))

                left += 1
                right -= 1

                while left < right and nums[left] == n_left:
                    left += 1  # skip duplicates

                while left < right and nums[right] == n_right:
                    right -= 1  # skip duplicates

            elif sum2 < target:
                left += 1

            else:  # sum2 > target
                right -= 1

    return result
