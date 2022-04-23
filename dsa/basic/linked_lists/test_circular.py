from basic.linked_lists.circular import *


def test_detects_circular_linked_lists():
    ll = LinkedList('a', 'b', 'c')
    a = Node('a')
    b = Node('b')
    c = Node('c')

    ll.head = a
    a.next = b
    b.next = c
    c.next = b

    assert circular(ll)


def test_detects_circular_linked_lists_linked_at_head():
    ll = LinkedList('a', 'b', 'c')
    a = Node('a')
    b = Node('b')
    c = Node('c')

    ll.head = a
    a.next = b
    b.next = c
    c.next = a

    assert circular(ll)


def test_detects_non_circular_linked_lists():
    ll = LinkedList('a', 'b', 'c')
    a = Node('a')
    b = Node('b')
    c = Node('c')

    ll.head = a
    a.next = b
    b.next = c
    c.next = None

    assert not circular(ll)
