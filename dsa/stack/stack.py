"""
Implementation of a Stack in Python.

"""
from __future__ import annotations

from dsa.node import Node

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')


@dataclass
class Stack(Generic[T]):
    """
    A simple Stack class.

    Hint: the `shift` and `unshift` methods from a Singly Linked List
    (basically to add/remove items from the start of a list) are defined
    as `push` and `pop` here, as these methods are supposed to be constant
    time - or **O(1)** - for Stacks.
    """

    # first: the initial item added on the stack
    first: Node | None = None

    # last: the most recent item added on the stack
    last: Node | None = None

    # size: the number of items in the stack
    size: int = 0

    def __init__(self, *values: T):
        for val in values:
            self.push(val)

    def push(self, val: T) -> int:
        """Add an item to the top of the stack. Returns the new stack size."""
        new_node = Node(val)
        # retrieve current item at top of the stack
        current_first = self.first
        # send new node to top of the stack
        self.first = new_node

        if not current_first:
            # if no items are in stack, set both `first` and `last` as current node
            self.last = new_node
        else:
            # else, set `next` on new node to the item previously at top of the stack
            self.first.next = current_first

        # increment the size, since we added a new item to the stack
        self.size += 1

        return self.size

    def pop(self) -> T:
        """Removes an item from the top of the stack. Follows a **LIFO** principle."""

        if not self.first:
            # if there are no items in the stack
            return None

        if self.size == 1:
            # clear `first` and `last`, as thew stack would now be empty
            self.last = None

        # retrieve item from top of the stack
        removed_item = self.first
        # move next item to top of the stack
        self.first = removed_item.next
        # decrement the size, since we removed an item from the stack
        self.size -= 1

        return removed_item.val
