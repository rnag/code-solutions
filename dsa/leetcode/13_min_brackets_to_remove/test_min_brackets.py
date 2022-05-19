from min_brackets import *


def test_min_remove_to_make_valid():
    assert min_remove_to_make_valid('') == ''
    assert min_remove_to_make_valid('))((') == ''
    assert min_remove_to_make_valid('a)bc(d)') == 'abc(d)'
    assert min_remove_to_make_valid('(ab(c)d') == 'ab(c)d'
