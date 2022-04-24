"""
1) Implement the Node class to create
a binary search tree.  The constructor
should initialize values 'val', 'left',
and 'right'.
2) Implement the 'insert' method for the
Node class.  Insert should accept an argument
'val', then create an insert a new node
at the appropriate location in the tree.
3) Implement the 'contains' method for the Node
class.  Contains should accept a 'val' argument
and return the Node in the tree with the same value.
"""
from __future__ import annotations

__all__ = ['Node']

from dataclasses import dataclass
from typing import TypeVar


T = TypeVar('T')


@dataclass
class Node:
    val: T
    left: Node | None = None
    right: Node | None = None

    def insert(self, val: T):
        """Insert a new node at the appropriate location in the tree."""

        if val == self.val:
            # duplicate, value already exists; no need ot add it
            return

        elif val < self.val:
            # *less than* current node's value: add node to the left
            if self.left:
                self.left.insert(val)
            else:  # no Node on the left exists, just add it in
                self.left = Node(val)

        else:
            # *greater than* current node's value: add node to the right
            if self.right:
                self.right.insert(val)
            else:  # no Node on the left exists, just add it in
                self.right = Node(val)

    def contains(self, val: T) -> Node | None:
        """
        Search through the tree to find a Node with the same value,
        if it exists.
        """

        if self.val == val:
            # value matches the current node's value, we are done
            return self

        elif val < self.val:
            # *less than* current node's value: look through the left side
            if self.left:
                return self.left.contains(val)

        else:
            # *greater than* current node's value: look through the right side
            if self.right:
                return self.right.contains(val)

        return None
