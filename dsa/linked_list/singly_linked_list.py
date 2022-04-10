"""
Copy this template and create a new example file from it as needed

"""
from __future__ import annotations

from dataclasses import dataclass
from pprint import pprint
from typing import Any


@dataclass
class Node:
    # val - piece of data
    val: Any
    # next - reference to next node
    next: Node | None = None


@dataclass
class SinglyLinkedList:
    head: Node | None = None
    tail: Node | None = None
    length: int = 0

    def push(self, val: Any) -> SinglyLinkedList:
        """Push new node to end of the linked list"""
        new_node = Node(val)

        if not self.head:
            # the linked list is empty (head/tail are both unset)
            self.head = new_node
        else:
            # set the current tail's `next` property to point to our new node
            self.tail.next = new_node

        # finally, set the new `tail` to point to our node
        self.tail = new_node
        # increment length
        self.length += 1

        return self

    # noinspection SpellCheckingInspection
    def unshift(self, val: Any) -> SinglyLinkedList:
        """Push new node to start of the linked list"""
        new_node = Node(val)

        if not self.head:
            # the linked list is empty (head/tail are both unset)
            self.tail = new_node
        else:
            # set the new head's `next` property to point to the current head
            new_node.next = self.head

        # finally, set the new `head` to point to our node
        self.head = new_node
        # increment length
        self.length += 1

        return self

    def pop(self) -> Node | None:
        """Remove (and return) current node at end of the linked list"""
        current = self.head
        new_tail = current

        if not current:
            # list is empty (head/tail are undefined)
            return None

        # loop while `next` property is defined (e.g. until we reach the tail)
        while current.next:
            # new tail lags behind `current` by ONE (1) node
            new_tail = current
            # increment `current` to point to the next node
            current = current.next

        # set the new tail on the linked list
        self.tail = new_tail
        self.tail.next = None

        # decrement length, since we removed an item
        self.length -= 1

        if not self.length:
            # was one item, now no items left
            self.head = self.tail = None

        return current

    def shift(self) -> Node | None:
        """Remove (and return) current node at start of the linked list"""
        if not self.head:
            # list is empty (head/tail are undefined)
            return None

        current_head = self.head
        self.head = current_head.next

        # (optional) unlink the `next` node from our current head
        current_head.next = None

        # decrement length, since we removed an item
        self.length -= 1

        if not self.length:
            # was one item, now no items left
            self.tail = None

        return current_head

    def get(self, index: int) -> Node | None:
        """Retrieve the node at the specified index."""
        if index < 0 or index >= self.length:
            # invalid index
            return None

        current = self.head
        counter = 0

        while counter != index:
            current = current.next
            counter += 1

        # alternate implementation:
        #   for i in range(1, index + 1):
        #       current = current.next

        return current

    def set(self, index: int, val: Any) -> bool:
        """Change the value of a node at the specified index."""
        found_node = self.get(index)

        if found_node:
            found_node.val = val
            return True

        # node at index not found
        return False

    def insert(self, index: int, val: Any) -> bool:
        """Insert a new node at the specified index."""
        if index < 0 or index > self.length:
            # invalid index
            return False

        if index == self.length:
            self.push(val)
            return True

        if index == 0:
            self.unshift(val)
            return True

        new_node = Node(val)
        prev = self.get(index - 1)

        current = prev.next
        prev.next = new_node
        new_node.next = current

        # increment length
        self.length += 1

        return True

    def remove(self, index: int) -> Node | None:
        """Remove (and return) a new node at the specified index."""
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.shift()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        removed = prev.next
        prev.next = removed.next

        # decrement length, since we removed an item
        self.length -= 1

        return removed

    def reverse(self) -> SinglyLinkedList:
        """Reverse the linked list *in place*."""

        # start at `head`
        current = self.head

        # swap the `head` and `tail` of the linked list
        self.head, self.tail = self.tail, self.head

        # initialize `prev` and `next` variables
        next = prev = None

        for i in range(self.length):
            # get the NEXT node that comes immediately after current
            # example: assume current node is `B` as shown below.
            # ------------- next  -|
            # -- current -|        |
            #             V        V
            #    A   ->   B   ->   C
            next = current.next
            # set `next` for the current node to point to the `previous` node
            # node that `prev` is basically the `current` node in our last iteration
            # -------- current -|
            # -- prev -|        |
            #          V        V
            #          A   <-   B   ->   C
            current.next = prev
            # increment pointers for `prev` and `current`
            #
            # now we repeat same process again in each loop iteration,
            # so polarity such as `B -> C` below is switched next time.
            # ---------- current  -|
            # ----- prev -|        |
            #             V        V
            #    A   <-   B   ->   C
            prev = current
            current = next

        return self

    # def pop(self) -> Node | None:
    #     """Remove (and return) current node at end of the linked list"""
    #     node = self.head
    #     last = self.tail
    #     ln = self.length
    #
    #     if not ln:
    #         return None
    #     elif ln == 1:
    #         self.head = self.tail = None
    #     else:
    #         while node:
    #             if node.next == last:
    #                 node.next = None
    #                 self.tail = node
    #                 break
    #             node = node.next
    #
    #     # decrement length, since we removed an item
    #     self.length -= 1
    #
    #     return last


