"""
Given a node, validate the binary search tree,
ensuring that every node's left hand child is
less than the parent node's value, and that
every node's right hand child is greater than
the parent.
"""
from __future__ import annotations

__all__ = ['Node',
           'validate']

from bst import Node


def validate(node: Node, min_val=None, max_val=None) -> bool:
    """confirm that we have a valid binary search tree."""

    if max_val is not None and node.val > max_val:
        return False

    if min_val is not None and node.val < min_val:
        return False

    if node.left and not validate(node.left, min_val, node.val):
        return False

    if node.right and not validate(node.right, node.val, max_val):
        return False

    return True
