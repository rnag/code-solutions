"""
1) Create a node class.  The constructor
should accept an argument that gets assigned
to the data property and initialize an
empty array for storing children. The node
class should have methods 'add' and 'remove'.

2) Create a tree class. The tree constructor
should initialize a 'root' property to null.

3) Implement 'traverseBF' and 'traverseDF'
on the tree class.  Each method should accept a
function that gets called with each element in the tree
"""
from __future__ import annotations

__all__ = ['Node',
           'Tree']

from collections import deque
from dataclasses import dataclass, field
from typing import TypeVar


T = TypeVar('T')


@dataclass
class Node:
    # val - piece of data
    val: T
    # children - reference to the *child* nodes
    children: list[Node] = field(default_factory=list)

    def add(self, val: T):
        node = Node(val)
        self.children.append(node)

    def remove(self, val: T):
        # alternatively, as a one-liner:
        #  self.children = [child for child in self.children if child.val != val]
        for i in range(len(self.children) - 1, -1, -1):
            if self.children[i].val == val:
                del self.children[i]


@dataclass
class Tree:
    root: Node | None = None

    def traverse_bf(self) -> list[T]:
        result = []
        arr = deque([self.root])

        while arr:
            node = arr.popleft()
            arr.extend(node.children)
            result.append(node.val)

        return result

    def traverse_df(self) -> list[T]:
        result = []
        arr = deque([self.root])

        while arr:
            node = arr.popleft()
            # `extendleft` appends elements in reverse order, so we need to
            # reverse the nodes first before passing it in.
            arr.extendleft(reversed(node.children))

            result.append(node.val)

        return result
