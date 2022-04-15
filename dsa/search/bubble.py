"""
Bubble Sort algorithm implementation in Python

This approach "bubbles up" the largest values to the end of the array.
On each iteration, the next largest value is moved up to its correct
place.
"""


# Bubble Sort solution
#
# Time complexity: O(N^2)
def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        no_swaps = True
        for j in range(i - 1):
            # print(arr, arr[j], arr[j+1])
            if arr[j] > arr[j + 1]:
                no_swaps = False
                # swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print('ONE PASS COMPLETE')
        if no_swaps:
            break
    return arr


def main():
    result = bubble_sort([8, 1, 2, 3, 4, 5, 6, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]

    l = [3, 2, 1, 7, 1]
    bubble_sort(l)
    assert l == [1, 1, 2, 3, 7]

    l = [37, 45, 29, 8, 12, 88, -3]
    bubble_sort(l)
    assert l == [-3, 8, 12, 29, 37, 45, 88]

    l = [7, 6, 5, 4, 3, 2, 1]
    bubble_sort(l)
    assert l == [1, 2, 3, 4, 5, 6, 7]


if __name__ == '__main__':
    main()
