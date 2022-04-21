from basic.vowels.vowels import vowels, vowels_idiomatic


def test_vowels_idiomatic():
    assert vowels_idiomatic('Hi There!') == 3
    assert vowels_idiomatic('Why do you ask?') == 4
    assert vowels_idiomatic('Why?') == 0
    assert vowels_idiomatic('aeiou') == 5
    assert vowels_idiomatic('AEIOU') == 5
    assert vowels_idiomatic('abcdefghijklmnopqrstuvwxyz') == 5
    assert vowels_idiomatic('bcdfghjkl') == 0


def test_vowels():
    assert vowels('Hi There!') == 3
    assert vowels('Why do you ask?') == 4
    assert vowels('Why?') == 0
    assert vowels('aeiou') == 5
    assert vowels('AEIOU') == 5
    assert vowels('abcdefghijklmnopqrstuvwxyz') == 5
    assert vowels('bcdfghjkl') == 0
