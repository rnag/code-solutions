"""
You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length
at that position.

Return `true` if you can reach the last index, or `false` otherwise.


Links:
    - https://leetcode.com/problems/jump-game/
    - https://youtu.be/Yan0cv2cLy8

"""
from __future__ import annotations

__all__ = ['can_jump',
           'can_jump_iterative']


def can_jump(nums: list[int]) -> bool:
    """
    Solution using a "greedy" algorithm

    Time complexity: O(N)
    Space complexity: O(1)
    """
    ln = len(nums)
    if ln < 2:
        return True

    goal = ln - 1

    for i in range(goal - 1, -1, -1):
        n = nums[i]
        if n + i >= goal:
            goal = i

    return goal == 0


def can_jump_iterative(nums: list[int]) -> bool:
    """
    Using iterative approach, via dynamic programming concepts.

    Time complexity: O(N^2)
    Space complexity: O(N)
    """
    n = len(nums)
    if n < 2:
        return True

    cache = {n - 1: True}

    for i in range(n - 2, -1, -1):
        num = nums[i]
        if num == 0:
            cache[i] = False
            continue

        for delta in range(1, num + 1):
            end = i + delta
            if cache[end]:
                cache[i] = True
                break
        else:  # no break statement was run
            cache[i] = False

    return cache[0]
