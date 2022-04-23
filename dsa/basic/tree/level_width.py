"""
Given the root node of a tree, return
an array where each element is the width
of the tree at each level.

--- Example
Given:
    0
  / |  \
1   2   3
|       |
4       5
Answer: [1, 3, 2]
"""
from __future__ import annotations

__all__ = ['Node',
           'level_width_idiomatic',
           'level_width_v1',
           'level_width_v2']

from collections import deque

from tree import Node


# stop character, can be anything, such as a string value 'S'
STOP = None


def level_width_idiomatic(root: Node) -> list[int]:
    arr = [root]
    temp_arr = []
    widths = [1]

    while arr:
        node = arr.pop(0)
        temp_arr.extend(node.children)

        if not arr and (num_children := len(temp_arr)):
            # alternatively:
            #   arr.extend(temp)
            arr = temp_arr
            widths.append(num_children)
            temp_arr = []

    return widths


def level_width_v1(root: Node) -> list[int]:
    arr = deque([STOP, root])
    result = []

    while arr:
        node = arr.popleft()
        if node is STOP:
            if num_children := len(arr):
                result.append(num_children)
                arr.append(STOP)
        else:
            arr.extend(node.children)

    return result


def level_width_v2(root: Node) -> list[int]:
    arr = deque([root, STOP])
    counters = [0]

    # loop while any node other than 'STOP' is in the list
    while len(arr) > 1:
        # remove first node
        node = arr.popleft()
        # check if it's a `STOP` marker
        if node is STOP:
            # move the `STOP` to the end of the list
            arr.append(STOP)
            # add new counter for level width
            counters.append(0)
        else:
            # else, it's a node, so add the node's children
            arr.extend(node.children)
            # increment the latest counter for level width
            counters[-1] += 1

    return counters
