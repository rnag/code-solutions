"""
Implement a Queue datastructure using two stacks.
*Do not* create an array inside the 'Queue' class.

Queue should implement the methods 'add' and 'remove'.

--- Examples
    q = Queue(1, 2);
    q.remove();  # returns 1
    q.remove();  # returns 2
"""
from __future__ import annotations

from stack.stack import Stack


class Queue:

    def __init__(self, *vals):
        self.first = Stack()
        self.second = Stack()

        for val in vals:
            self.add(val)

    def add(self, val):
        self.first.push(val)

    def remove(self):
        # move over everything from *first* to *second* stack
        while self.first.first is not None:
            self.second.push(self.first.pop())

        # remove first element from *second* stack
        removed = self.second.pop()

        # restore *first* stack
        while self.second.first is not None:
            self.first.push(self.second.pop())

        return removed
