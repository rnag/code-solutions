"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


https://leetcode.com/problems/merge-k-sorted-lists/

"""
from __future__ import annotations

__all__ = ['ListNode',
           'merge_k_lists']

from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False

        return self.val == other.val and self.next == other.next

# uncomment for submission to Leetcode
# class Wrapper:
#     def __init__(self, node):
#         self.node = node
#         self.val = node.val
#
#     def __lt__(self, other):
#         return self.val < other.val


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    head = point = ListNode(0)
    q = PriorityQueue()

    for l in lists:
        if l:
            q.put(l)
            # q.put(Wrapper(l))

    while not q.empty():
        node: ListNode = q.get()
        # node = q.get().node

        point.next = node

        point = point.next
        node = node.next

        if node:
            q.put(node)
            # q.put(Wrapper(node))

    return head.next
