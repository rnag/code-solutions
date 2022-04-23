"""
Given a linked list, return the element `n` spaces
from the last node in the list.  Do not call the 'size'
method of the linked list.  Assume that `n` will always
be less than the length of the list.

--- Examples
   ll = LinkedList('a', 'b', 'c', 'd')
   from_last(ll, 2).val  # 'b'
"""
from __future__ import annotations

__all__ = ['LinkedList',
           'Node',
           'from_last']

from linked_list.singly_linked_list import SinglyLinkedList as LinkedList
from node import Node


def from_last(ll: LinkedList, n: int) -> Node | None:
    # assign both `slow` and `fast` to the first node in the list
    slow = fast = ll.head

    # advance `fast`, so it is ahead of `slow` by `n` nodes
    for i in range(n):
        fast = fast.next

    # loop while the next *two* nodes after `fast` exist
    while fast.next:
        # advance `slow` by *one* node
        slow = slow.next
        # advance `fast` by *one* node
        fast = fast.next

    return slow
