from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Generic, TypeVar


T = TypeVar('T')


@dataclass
class Node:
    # val - piece of data
    val: Any
    # left - reference to the node on LEFT side
    left: Node | None = None
    # right - reference to the node on RIGHT side
    right: Node | None = None


@dataclass
class BinarySearchTree(Generic[T]):
    root: Node | None = None

    def insert(self, val: T) -> BinarySearchTree | None:
        """Insert a new node in the Binary Search Tree (BST)"""
        new_node = Node(val)

        if not self.root:
            self.root = new_node
            return self

        current = self.root

        while True:
            if val == current.val:
                # it's a duplicate
                return None

            if val < current.val:
                # goes on the left side
                if current.left is None:
                    # nothing on `left` side, add it and we're DONE
                    current.left = new_node
                    return self
                # else, set `current` to the `left` node
                current = current.left

            else:
                # goes on the right side
                if current.right is None:
                    # nothing on `right` side, add it and we're DONE
                    current.right = new_node
                    return self
                # else, set `current` to the `right` node
                current = current.right

    def find(self, val: T) -> Node | None:
        """Retrieve a node from the Binary Search Tree (BST)"""
        if not self.root:
            return None

        current = self.root
        found = False

        while current and not found:

            if val == current.val:
                # we found it, so we're DONE
                #
                # alternatively, we *could* just return the found node here:
                #   return current
                found = True

            elif val < current.val:
                current = current.left
            else:
                current = current.right

        return current if found else None

    def BFS(self):
        """breadth-first search (HORIZONTAL before VERTICAL)"""
        data = []
        queue = [self.root]

        while queue:
            node = queue.pop(0)
            data.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return data

    def DFS_pre_order(self):
        """depth-first search (VERTICAL before HORIZONTAL)"""
        data = []
        current = self.root

        def traverse(node: Node):
            data.append(node.val)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(current)

        return data

    def DFS_post_order(self):
        """depth-first search (VERTICAL before HORIZONTAL)"""
        data = []
        current = self.root

        def traverse(node: Node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node.val)

        traverse(current)

        return data

    def DFS_in_order(self):
        """depth-first search (VERTICAL before HORIZONTAL)"""
        data = []
        current = self.root

        def traverse(node: Node):
            if node.left:
                traverse(node.left)

            data.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(current)

        return data
