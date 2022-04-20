from basic.palindrome.palindrome import palindrome


def test_palindrome():
    assert palindrome('abba')
    assert not palindrome('abcdefg')
