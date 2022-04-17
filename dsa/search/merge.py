"""
Merge Sort algorithm implementation in Python

Combination of:
    - Splitting up
    - Sorting
    - Merging

It exploits the fact that arrays of 0 or 1 element are always sorted.
"""


def merge(arr1: list, arr2: list) -> list:
    """
    Helper function to merge two sorted arrays, and return a new array
    which is also sorted.

    This function runs in O(M+N) time and space complexity, where `M` and `N`
    are the size of the input arrays respectively.
    """
    merged = []
    i = 0
    j = 0
    ln1, ln2 = len(arr1), len(arr2)

    while i < ln1 and j < ln2:
        e1, e2 = arr1[i], arr2[j]
        if e1 == e2:
            i += 1
            j += 1
            merged.append(e1)
            merged.append(e2)
        elif e1 < e2:
            i += 1
            merged.append(e1)
        else:   # e2 < e1
            j += 1
            merged.append(e2)

    if i < ln1:
        merged.extend(arr1[i:])

    if j < ln2:
        merged.extend(arr2[j:])

    return merged


# Merge Sort solution
#
# Time complexity: O(N log N) - Best, Average, Worst
#   - We have `log N` decompositions, and `N` comparisons in each decomposition.
# Space complexity: O(N)
def merge_sort(arr):
    lr = len(arr)

    # base case: if the array has 1 element or less, it's already sorted
    if lr <= 1:
        return arr

    # get midway point from array, and split on left and right side
    # call `merge_sort` recursively on each half.
    mid = lr // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge the two sorted arrays (left and right part)
    return merge(left, right)


def main():

    result = merge_sort([8, 3, 5, 4, 7, 6, 1, 2])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]

    result = merge_sort([8, 1, 2, 3, 4, 5, 6, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]

    l = [3, 2, 1, 7, 1]
    result = merge_sort(l)
    assert result == [1, 1, 2, 3, 7]

    l = [37, 45, 29, 8, 12, 88, -3]
    result = merge_sort(l)
    assert result == [-3, 8, 12, 29, 37, 45, 88]

    l = [7, 6, 5, 4, 3, 2, 1]
    result = merge_sort(l)
    assert result == [1, 2, 3, 4, 5, 6, 7]


if __name__ == '__main__':
    main()
