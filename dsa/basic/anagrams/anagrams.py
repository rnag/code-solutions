"""
Check to see if two provided strings are anagrams of each other.

One string is an anagrams of another if it uses the same characters
in the same quantity. Only consider characters, not spaces
or punctuation.  Consider capital letters to be the same as lower case.

--- Examples
  anagrams('rail safety', 'fairy tales') --> True
  anagrams('RAIL! SAFETY!', 'fairy tales') --> True
  anagrams('Hi there', 'Bye there') --> False
"""
from collections import defaultdict


def anagrams_optimized(s1: str, s2: str) -> bool:
    # empty strings are considered equal
    if not s1 and not s2:
        return True

    # lowercase both strings, so comparisons can be case-insensitive
    s1 = s1.lower()
    s2 = s2.lower()

    freq = defaultdict(int)

    for c in s1:
        if c.isalpha():  # only consider alphabetic characters
            freq[c] += 1

    for c in s2:
        if not c.isalpha():  # only consider alphabetic characters
            continue

        c_count = freq[c]
        if not c_count:
            return False

        freq[c] = c_count - 1

    return True


def anagrams(s1: str, s2: str) -> bool:
    return clean_string(s1) == clean_string(s2)


# helper function to return sort alphabetic characters in a string
def clean_string(s: str) -> str:
    return ''.join(sorted(c for c in s.lower() if c.isalpha()))
