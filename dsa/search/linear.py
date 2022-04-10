"""
Write a function `linear_search` that accepts an array and a value.

Loop through the array and check if the current element is equal to value;
if it is, return the index at which the element is found.

If the value is never found, return -1.
"""


def linear_search(arr, val):
    for i, n in enumerate(arr):
        if n == val:
            return i

    return -1


if __name__ == '__main__':
    assert linear_search([1, 2, 3, 4], 3) == 2
