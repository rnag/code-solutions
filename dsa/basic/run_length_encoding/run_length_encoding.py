"""
Calculate the run length encoding - typically of an image.

Run length encoding was an older lossless compression algorithm from the '60s,
which was a way to compress image files - if you think of an image file as
just a series of pixels.

"""

from __future__ import annotations

__all__ = ['encode']


#
# Time complexity: O(N)
def encode(s: str) -> str:

    # check for an empty string
    if not s:
        return s

    prev_char = s[0]
    count = 1
    ret = ''

    # iterate over input
    for c in s[1:]:
        if c == prev_char:
            count += 1
        else:
            # alternatively:
            #   ret += f'{count}{prev_char}'
            ret = f'{ret}{count}{prev_char}'
            prev_char = c
            count = 1

    ret = f'{ret}{count}{prev_char}'

    return ret
