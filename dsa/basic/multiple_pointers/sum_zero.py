"""
Write a function sum_zero which accepts a sorted array of integers.

The function should find the first pair where the sum is 0. Return a
tuple that includes both values that sum to zero or undefined if a
pair does not exist.

"""


# Naive solution:
#   Time complexity - O(N^2)
#   Space complexity - O(1)
def sum_zero_naive(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if not arr[i] + arr[j]:
                return arr[i], arr[j]

    # no such pairs found, return explicit None
    return None


# Multiple pointers pattern:
#   Time complexity - O(N) *worst case*
#   Space complexity - O(1)
def sum_zero(arr):
    left = 0
    right = len(arr) - 1

    while right > left:     # or: while left < right
        n1 = arr[left]
        n2 = arr[right]
        sum_n = n1 + n2

        if not sum_n:
            # nothing, we are done!
            return n1, n2

        elif sum_n > 0:
            # sum is too high, so we need to decrease `j`
            right -= 1

        else:
            # sum is too less (negative), so we need to increase `i`
            left += 1

    # no such pairs found, return explicit None
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert sum_zero([-3, 0, 2, 3]) == (-3, 3)
    assert sum_zero([-7, -2, 1, 2, 3, 5]) == (-2, 2)
    assert sum_zero([-3, 3, 2]) is None
    assert sum_zero([-4, -3, -2, -1, 0, 1, 2, 3, 10]) == (-3, 3)
    assert sum_zero([-4, -3, -2, -1, 0, 5, 10]) is None
