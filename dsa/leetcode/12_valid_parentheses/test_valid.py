from valid import *


def test_is_valid_parentheses():
    assert not is_valid_parentheses('({[]')
    assert not is_valid_parentheses('({[])}')
    assert is_valid_parentheses('({[]})')
    assert is_valid_parentheses('{()[]}')
    assert is_valid_parentheses('{()[]}')

