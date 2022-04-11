from collections import defaultdict


def char_count(s: str):
    """Count occurrences of each character in an input string."""

    freq = defaultdict(int)
    # lowercase the string, so we can normalize `A-Z` to `a-z`
    s = s.lower()

    for c in s:
        # if the character is alpha-numeric
        if c.isalnum():
            freq[c] += 1

    return freq


if __name__ == '__main__':

    assert char_count('Hello, world!') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    assert char_count('') == {}
    assert char_count('hi') == {'h': 1, 'i': 1}
    assert char_count('whatsuphomiehowareyou') == {
        'w': 2, 'h': 3, 'a': 2, 't': 1, 's': 1, 'u': 2, 'p': 1, 'o': 3, 'm': 1,
        'i': 1, 'e': 2, 'r': 1, 'y': 1
    }
