from first_non_repeating_char import *


def test_first_non_repeating_character():
    assert first_non_repeating_character('') == '_'
    assert first_non_repeating_character('aa') == '_'
    assert first_non_repeating_character('b') == 'b'
    assert first_non_repeating_character('aaabcccdeeef') == 'b'
    assert first_non_repeating_character('abacabad') == 'c'
    assert first_non_repeating_character('abcabcabc') == '_'
    assert first_non_repeating_character('aabbbc') == 'c'
    assert first_non_repeating_character('aabbbcc') == '_'
