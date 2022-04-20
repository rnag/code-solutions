"""
Given a string, return the character that is most
commonly used in the string.

--- Examples
  maxChar("abcccccccd") === "c"
  maxChar("apple 1231111") === "1"
"""
from collections import defaultdict


def max_char(s: str) -> str:
    freq_count = defaultdict(int)
    # max character and occurrences of the character
    max_ch = None
    max_count = 0

    # loop over each character in the string
    for ch in s:
        new_count = freq_count[ch] + 1
        # check if character count is more than `max_count`, if so set
        # `max_char` to this character. Note that we could also put this
        # logic in a separate `for` loop, where we iterate over `freq_count`.
        if new_count > max_count:
            max_count = new_count
            max_ch = ch
        # increment the occurrence for the character
        freq_count[ch] = new_count

    return max_ch
