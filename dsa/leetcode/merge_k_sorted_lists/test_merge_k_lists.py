from __future__ import annotations

from merge_k_lists import *


def make_linked_lists(*lists: list[int]) -> list[ListNode]:
    lls = []
    for l in lists:
        ll = point = ListNode(0)

        for elem in l:
            node = ListNode(elem)
            point.next = node
            point = point.next

        ll = ll.next
        lls.append(ll)

    return lls


def test_merge_k_lists():
    ll = make_linked_lists([1, 4, 5], [1, 3, 4], [2, 6])
    ll_merged = make_linked_lists([1, 1, 2, 3, 4, 4, 5, 6])[0]

    res = merge_k_lists(ll)
    assert res == ll_merged
