

def same_naive(arr1, arr2):
    """
    Check if every value in the array `arr1` has its corresponding value squared
    in the second array `arr2`.

    The frequency of values must be the same.

    Time complexity: O(N ^ 2)
    """
    ln1 = len(arr1)

    if ln1 != len(arr2):
        return False

    for i in range(ln1):
        try:
            arr2.remove(arr1[i] ** 2)
        except ValueError:
            # number is not in array
            return False

    return True


if __name__ == '__main__':
    assert same_naive([1, 1, 1], [1, 1, 1])
    assert not same_naive([1, 1, 1], [1, 1, 3])
    assert same_naive([2, 2, 3], [4, 9, 4])
    assert not same_naive([2, 1, 2, 1], [2, 1, 2])
