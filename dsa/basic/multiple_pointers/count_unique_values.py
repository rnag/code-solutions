"""
Implement a function called `count_unique_values` which accepts a sorted
array, and counts the unique values in the array.

There can be negative numbers in the array, but it will always be sorted.

"""
__all__ = ['count_unique_values_single_ptr',
           'count_unique_values']


def count_unique_values_single_ptr(arr):
    prev_num = None
    count = 0

    for num in arr:
        if num == prev_num:
            continue

        prev_num = num
        count += 1

    return count


def count_unique_values(arr):
    # i starts at 0, the first index essentially.
    # j starts at `i+1`, and essentially "leads" the way through the array.
    i = 0
    len_arr = len(arr)

    if not len_arr:  # array is empty
        return 0

    for j in range(1, len_arr):
        n1 = arr[i]
        n2 = arr[j]

        if n1 != n2:
            # replace element at `i+1` with new number, and increment i
            i += 1
            arr[i] = n2

    return i + 1


def count_unique_values_alt(arr):
    # i starts at 0, the first index essentially.
    # j starts at `i+1`, and essentially "leads" the way through the array.
    i, j = 0, 1

    len_arr = len(arr)

    if not len_arr:  # array is empty
        return 0

    while j < len_arr:
        n1 = arr[i]
        n2 = arr[j]

        if n1 == n2:
            # nothing to do, increment `j` so it moves up the array
            j += 1
        else:
            # replace element at `i+1` with new number, and increment i
            i += 1
            arr[i] = n2

    return i + 1


if __name__ == '__main__':
    assert count_unique_values([1, 1, 1, 1, 2]) == 2
    assert count_unique_values([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]) == 7
    assert count_unique_values([]) == 0
    assert count_unique_values([7]) == 1
    assert count_unique_values([-2, -1, -1, 0, 1]) == 4
