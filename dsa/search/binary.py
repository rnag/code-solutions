"""
Write a function `binary_search` that accepts a (sorted) array and a value.

Use a *divide and conquer* approach. Since the array is already sorted, we can
use a halfway point in the array each time, and then check if the number to
search is less than or greater than the value at that index.

If less than, we eliminate the top half of that array; if greater than, we can
eliminate the bottom half of the array. Then we continue, taking the halfway
point and repeating the process until we find the element we're searching for.

If the current element is equal to value, we return the index at which the
element is found.

If the value is never found, return -1.
"""


# Binary Search solution
#
# Time complexity:
#   Best case - O(1)
#   Worst case - O(log N)
#   Average - O(log N)
def binary_search(arr, val):
    start = 0
    end = len(arr) - 1

    while end >= start:
        # pivot point, set this to *midway* point between `start` and `end`
        mid = (start + end) // 2
        # get the element at the pivot point
        n = arr[mid]

        if val == n:
            # nothing to do, we're done
            return mid

        elif val < n:
            # less than pivot point, so only consider the first half
            end = mid - 1

        else:
            # greater than pivot point, so only consider the upper half
            start = mid + 1

    # element is not found
    return -1


if __name__ == '__main__':
    assert binary_search([1, 3, 4, 6, 8, 9, 11, 12, 15, 16, 17, 18, 19], 15) == 8
    assert binary_search([1, 2, 3, 4], 3) == 2
    assert binary_search([1, 2, 3, 4], 6) == -1
    assert binary_search([], 6) == -1
