from basic.chunk.chunk import chunk, chunk_idiomatic


def test_chunk_idiomatic():
    assert chunk_idiomatic([1, 2, 3], 4) == [[1, 2, 3]]
    assert chunk_idiomatic([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk_idiomatic([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_idiomatic([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert chunk_idiomatic([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [5]]
    assert chunk_idiomatic([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]


def test_chunk():
    assert chunk([1, 2, 3], 4) == [[1, 2, 3]]
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) == [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert chunk([1, 2, 3, 4, 5], 4) == [[1, 2, 3, 4], [5]]
    assert chunk([1, 2, 3, 4, 5], 10) == [[1, 2, 3, 4, 5]]
