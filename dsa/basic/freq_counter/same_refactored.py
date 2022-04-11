import math
from collections import defaultdict


def same_refactored(arr1, arr2):
    """
    Check if every value in the array `arr1` has its corresponding value squared
    in the second array `arr2`.

    The frequency of values must be the same.

    Time complexity: O(N)
    """
    if len(arr1) != len(arr2):
        return False

    freq_count = defaultdict(int)

    for n in arr2:
        freq_count[n] += 1

    for n in arr1:
        new_freq = freq_count[n ** 2] - 1

        if new_freq < 0:
            return False

        freq_count[n] = new_freq

    return True


if __name__ == '__main__':
    assert same_refactored([1, 1, 1], [1, 1, 1])
    assert not same_refactored([1, 1, 1], [1, 1, 3])
    assert same_refactored([2, 2, 3], [4, 9, 4])
    assert not same_refactored([2, 1, 2, 1], [2, 1, 2])
