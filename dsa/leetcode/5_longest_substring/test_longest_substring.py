from longest_substring import *


def test_longest_substring():
    assert longest_substring('abccabb') == 3
    assert longest_substring('cccccc') == 1
    assert longest_substring('') == 0
    # below substrings are `abc` and `cbda`, max length is 4
    assert longest_substring('abcbda') == 4
    assert longest_substring('abcbdaac') == 4
    assert longest_substring('abcbbd') == 3


def test_longest_substring_optimized():
    assert longest_substring_optimized('abccabb') == 3
    assert longest_substring_optimized('cccccc') == 1
    assert longest_substring_optimized('') == 0
    # below substrings are `abc` and `cbda`, max length is 4
    assert longest_substring_optimized('abcbda') == 4
    assert longest_substring_optimized('abcbdaac') == 4
    assert longest_substring_optimized('abcbbd') == 3
