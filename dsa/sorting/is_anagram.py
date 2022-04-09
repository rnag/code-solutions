"""
Given two strings, write a function to determine if the second string
is an anagram of the first.

An example of an anagram: "cinema" <-> "iceman"

"""
from collections import defaultdict


def valid_anagram(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    # if the words are different lengths, they can't be equal
    if len1 != len2:
        return False

    # empty strings are equal, and we don't need to run anything else
    if not len1 and not len2:
        return True

    freq1 = defaultdict(int)
    freq2 = defaultdict(int)

    for c in word1:
        freq1[c] += 1

    for c in word2:
        freq2[c] += 1

    return freq1 == freq2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert valid_anagram('', '')                    # True
    assert not valid_anagram('aaz', 'zza')          # False
    assert valid_anagram('anagram', 'nagaram')      # True
    assert not valid_anagram('rat', 'car')          # False
    assert not valid_anagram('awesome', 'awesom')   # False
    assert valid_anagram('qwerty', 'qeywrt')        # True
    assert valid_anagram('cinema', 'iceman')        # True
