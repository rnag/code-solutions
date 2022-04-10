"""
Simple definition of a (reusable) Node class.

"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    # val - piece of data
    val: Any
    # next - reference to next node
    next: Node | None = None


if __name__ == '__main__':
    from pprint import pprint

    n = Node('hello')
    n.next = Node('there')
    n.next.next = Node('how')
    n.next.next.next = Node('are')
    n.next.next.next.next = Node('you')

    pprint(n)
