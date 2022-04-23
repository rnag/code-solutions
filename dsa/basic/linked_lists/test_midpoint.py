from basic.linked_lists.midpoint import *


def test_midpoint_when_3_elements():
    ll = LinkedList('a', 'b', 'c')

    assert midpoint(ll).val == 'b'


def test_midpoint_when_5_elements():
    ll = LinkedList('a', 'b', 'c', 'd', 'e')

    assert midpoint(ll).val == 'c'


def test_midpoint_when_16_elements():
    ll = LinkedList('aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh',
                    'ii', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq')

    assert midpoint(ll).val == 'hh'
