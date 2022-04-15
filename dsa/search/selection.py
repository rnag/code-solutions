"""
Selection Sort algorithm implementation in Python

Similar to Bubble Sort, but instead of first placing large values into
sorted position, this places *small* values into sorted position.
"""


# Selection Sort solution
#
# Time complexity: O(N^2)
def selection_sort(arr):
    lr = len(arr)

    for i in range(lr):
        smallest = i
        # loop over from `i + 1`, since smallest already points to `i`
        for j in range(i + 1, lr):
            # print(i, j)
            if arr[j] < arr[smallest]:
                smallest = j
        # if there is a new `smallest`, swap the values at the indices
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


def main():
    result = selection_sort([8, 1, 2, 3, 4, 5, 6, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]

    l = [3, 2, 1, 7, 1]
    selection_sort(l)
    assert l == [1, 1, 2, 3, 7]

    l = [37, 45, 29, 8, 12, 88, -3]
    selection_sort(l)
    assert l == [-3, 8, 12, 29, 37, 45, 88]

    l = [7, 6, 5, 4, 3, 2, 1]
    selection_sort(l)
    assert l == [1, 2, 3, 4, 5, 6, 7]


if __name__ == '__main__':
    main()
