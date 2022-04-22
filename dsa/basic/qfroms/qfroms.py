"""
--- Directions
Implement a Queue datastructure using two stacks.
*Do not* create an array inside the 'Queue' class.

Queue should implement the methods 'add' and 'remove'.

--- Examples
    const q = new Queue(1, 2);
    q.remove();  # returns 1
    q.remove();  # returns 2
"""
from __future__ import annotations

from stack.stack import Stack


class Queue:

    def __init__(self, *vals):
        self.s1 = Stack()
        self.s2 = Stack()

        for val in vals:
            self.add(val)

    def add(self, val):
        self.s1.push(val)

    def remove(self):
        # move over everything from stack A to stack B
        while self.s1.first is not None:
            self.s2.push(self.s1.pop())

        # remove first element from stack B
        removed = self.s2.pop()

        # restore stack A
        while self.s2.first is not None:
            self.s1.push(self.s2.pop())

        return removed
