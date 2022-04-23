from basic.linked_lists.from_last import *


def test_from_last_1():
    ll = LinkedList('a', 'b', 'c', 'd')
    assert from_last(ll, 2).val == 'b'


def test_from_last_2():
    ll = LinkedList('a', 'b', 'c', 'd', 'e')
    assert from_last(ll, 3).val == 'b'
