"""
Write a function called `max_sub_array_sum` which accepts an array of
integers and a number called `n`. The function should calculate the
maximum sum of `n` consecutive elements in the array.

"""

__all__ = ['max_sub_array_sum',
           'max_sub_array_sum_naive']


# Sliding window solution:
#   Time complexity - O(N)
#   Space complexity - O(1)
def max_sub_array_sum(arr, n):
    ln = len(arr)

    # if `n` is more than length of arr, then return None
    if n > ln:
        return None

    max_sum = temp_sum = sum(arr[:n])

    for i in range(n, ln):
        temp_sum = temp_sum - arr[i - n] + arr[i]

        # alternatively:
        #   max_sum = max(max_sum, temp_sum)
        if temp_sum > max_sum:
            max_sum = temp_sum

    return max_sum


# Naive solution:
#   Time complexity - O(N^2)
#   Space complexity - O(1)
def max_sub_array_sum_naive(arr, n):
    ln = len(arr)

    # if `n` is more than length of arr, then return None
    if n > ln:
        return None

    max = float('-inf')

    for i in range(ln - n + 1):
        temp = 0

        for j in range(n):
            temp += arr[i + j]

        if temp > max:
            max = temp

    return max
