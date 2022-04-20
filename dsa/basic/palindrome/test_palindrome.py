from basic.palindrome.palindrome import palindrome, palindrome_optimized


def test_palindrome():
    assert palindrome('abba')
    assert palindrome('RACECAR')
    assert not palindrome('abcdefg')


def test_palindrome_optimized():
    assert palindrome_optimized('abba')
    assert palindrome_optimized('RACECAR')
    assert not palindrome_optimized('abcdefg')
