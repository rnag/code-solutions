"""
Write a function that returns the number of vowels
used in a string.  Vowels are the characters 'a', 'e'
'i', 'o', and 'u'.

--- Examples
  vowels('Hi There!') --> 3
  vowels('Why do you ask?') --> 4
  vowels('Why?') --> 0
"""
_VOWELS = 'aeiouAEIOU'


def vowels_idiomatic(s: str) -> int:
    return len([ch for ch in s if ch in _VOWELS])


def vowels(s: str) -> int:
    vowel_count = 0

    for ch in s:
        if ch in _VOWELS:
            vowel_count += 1

    return vowel_count
