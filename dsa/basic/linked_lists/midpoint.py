"""
Return the 'middle' node of a linked list.
If the list has an even number of elements, return
the node at the end of the first half of the list.

*Do not* use a counter variable, *do not* retrieve
the size of the list, and only iterate
through the list one time.

--- Example
  l = LinkedList('a', 'b', 'c');
  midpoint(l);  # returns { data: 'b' }
"""
from __future__ import annotations

__all__ = ['LinkedList',
           'midpoint']

from linked_list.singly_linked_list import SinglyLinkedList as LinkedList


def midpoint(ll: LinkedList):
    # assign both `slow` and `fast` to the first node in the list
    slow = fast = ll.head

    # loop while the next *two* nodes after `fast` exist
    while fast.next and fast.next.next:
        # advance `slow` by *one* node
        slow = slow.next
        # advance `fast` by *two* nodes
        fast = fast.next.next

    return slow
