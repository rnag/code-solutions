"""
Given a linked list, return true if the list
is circular, false if it is not.

--- Examples
    ll = LinkedList('a', 'b', 'c')
    a = Node('a')
    b = Node('b')
    c = Node('c')

    ll.head = a
    a.next = b
    b.next = c
    c.next = b
"""
from __future__ import annotations

__all__ = ['LinkedList',
           'Node',
           'circular']

from linked_list.singly_linked_list import SinglyLinkedList as LinkedList
from node import Node


def circular(ll: LinkedList):
    # assign both `slow` and `fast` to the first node in the list
    slow = fast = ll.head

    # loop while the next *two* nodes after `fast` exist
    while fast.next and fast.next.next:
        # advance `slow` by *one* node
        slow = slow.next
        # advance `fast` by *two* nodes
        fast = fast.next.next
        # are both `slow` and `fast` pointing at the *same* node?
        if slow == fast:
            # if so, we have a circular linked list
            return True

    return False
