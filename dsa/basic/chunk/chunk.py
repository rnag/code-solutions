"""
Given an array and chunk size, divide the array into many sub-arrays
where each sub-array is of length `size`

--- Examples
chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
"""
import math


def chunk_idiomatic(arr: list, size: int) -> list:
    return [arr[i * size:i * size + size]
            for i in range(math.ceil(len(arr) / size))]


def chunk(arr: list, size: int) -> list:
    chunked = []

    for elem in arr:
        try:                # get last chunk
            last = chunked[-1]
        except IndexError:  # list is empty
            chunked.append([elem])
        else:
            if len(last) == size:  # sub-array is full, create a new one
                chunked.append([elem])
            else:                  # add on to the last sub-array
                last.append(elem)

    return chunked
