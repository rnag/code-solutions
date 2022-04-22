"""
Implementation of a Queue in Python.

"""
from __future__ import annotations

from dsa.node import Node

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar('T')


@dataclass
class Queue(Generic[T]):
    """
    A simple Queue class.

    Hint: the `enqueue` and `dequeue` methods from a Singly Linked List
    (basically to add/remove items from the start of a list) are defined
    as `push` and `pop` here, as these methods are supposed to be constant
    time - or **O(1)** - for Queues.
    """

    # first: the initial item added on the queue
    first: Node | None = None

    # last: the most recent item added on the queue
    last: Node | None = None

    # size: the number of items in the queue
    size: int = 0

    def __init__(self, *values: T):
        for val in values:
            self.enqueue(val)

    def enqueue(self, val: T) -> int:
        """Add an item to the end of the queue. Returns the new queue size."""
        new_node = Node(val)
        # retrieve current item at end of the queue
        current_last = self.last
        # send new node to end of the queue
        self.last = new_node

        if not current_last:
            # if no items are in queue, set both `first` and `last` as current node
            self.first = new_node
        else:
            # else, set `next` on the previous item at end of the queue to the new node
            current_last.next = new_node

        # increment the size, since we added a new item to the queue
        self.size += 1

        return self.size

    def dequeue(self) -> T:
        """Removes an item from the top of the queue. Follows a **LIFO** principle."""

        if not self.first:
            # if there are no items in the queue
            return None

        if self.size == 1:
            # clear `first` and `last`, as thew queue would now be empty
            self.last = None

        # retrieve item from top of the queue
        removed_item = self.first
        # move next item to top of the queue
        self.first = removed_item.next
        # decrement the size, since we removed an item from the queue
        self.size -= 1

        return removed_item.val
