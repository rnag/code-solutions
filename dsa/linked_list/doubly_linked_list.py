"""
Almost identical to Singly Linked lists, except *every* node
has **another** pointer, to the `previous` node.

# Downsides
A doubly linked list takes up **more memory**, because it *also* has
a pointer to the `previous` node.

"""
from __future__ import annotations

from dsa.node import Node

from dataclasses import dataclass
from typing import Any


@dataclass
class Node(Node):
    # prev - reference to previous node
    prev: Node | None = None


@dataclass
class DoublyLinkedList:
    head: Node | None = None
    tail: Node | None = None
    length: int = 0

    def push(self, val: Any) -> DoublyLinkedList:
        """Push new node to end of the linked list"""
        new_node = Node(val)

        if not self.head:
            # the linked list is empty (head/tail are both unset)
            self.head = new_node
        else:
            # set the current tail's `next` property to point to our new node
            self.tail.next = new_node
            # set the new tail's `prev` property to point to our current tail
            new_node.prev = self.tail

        # finally, set the new `tail` to point to our node
        self.tail = new_node
        # increment length
        self.length += 1

        return self

    # noinspection SpellCheckingInspection
    def unshift(self, val: Any) -> DoublyLinkedList:
        """Push new node to start of the linked list"""
        new_node = Node(val)

        if not self.head:
            # the linked list is empty (head/tail are both unset)
            self.tail = new_node
        else:
            # set the current head's `prev` property to point to our current head
            self.head.prev = new_node
            # set the new head's `next` property to point to the current head
            new_node.next = self.head

        # finally, set the new `head` to point to our node
        self.head = new_node
        # increment length
        self.length += 1

        return self

    def pop(self) -> Node | None:
        """Remove (and return) current node at end of the linked list"""

        if not self.head:
            # list is empty (head/tail are undefined)
            return None

        popped_node = self.tail

        if self.length == 1:
            # was one item, now no items left
            self.head = self.tail = None
        else:
            # set the new tail on the linked list
            self.tail = popped_node.prev
            self.tail.next = None
            # for returned node, we should clear or unlink the `previous` node
            popped_node.prev = None

        # decrement length, since we removed an item
        self.length -= 1

        return popped_node

    def shift(self) -> Node | None:
        """Remove (and return) current node at start of the linked list"""
        if not self.head:
            # list is empty (head/tail are undefined)
            return None

        current_head = self.head

        if self.length == 1:
            # was one item, now no items left
            self.head = self.tail = None
        else:
            self.head = current_head.next
            # clear the `previous` node from our new head
            self.head.prev = None
            # (optional) unlink the `next` node from our current head
            current_head.next = None

        # decrement length, since we removed an item
        self.length -= 1

        return current_head

    def get(self, index: int) -> Node | None:
        """Retrieve the node at the specified index."""
        if index < 0 or index >= self.length:
            # invalid index
            return None

        count = current = None

        if index <= self.length // 2:
            # starting from the start of linked list
            current = self.head
            count = 0

            while count != index:
                current = current.next
                count += 1
        else:
            # starting from the end of linked list
            current = self.tail
            count = self.length - 1

            while count != index:
                current = current.prev
                count -= 1

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

        # get `before` and `after` nodes
        prev = self.get(index - 1)
        next = prev.next
        # update `next` and `prev` in existing nodes to point to new node
        prev.next = new_node
        next.prev = new_node
        # add `next` and `prev` connections for new node
        new_node.prev = prev
        new_node.next = next

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

        removed_node = self.get(index)
        # retrieve the `before` and `after` nodes
        prev = removed_node.prev
        next = removed_node.next

        prev.next = next
        next.prev = prev

        # (optional) unlink the `next` and `prev` node from our removed node
        removed_node.next = removed_node.prev = None

        # decrement length, since we removed an item
        self.length -= 1

        return removed_node

    def reverse(self) -> DoublyLinkedList:
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


