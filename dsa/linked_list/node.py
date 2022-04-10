"""
Copy this template and create a new example file from it as needed

"""
from dataclasses import dataclass
from pprint import pprint
from typing import Any


@dataclass
class Node:
    # val - piece of data
    val: Any
    # next - reference to next node
    next: 'Node' = None


n = Node('hello')
n.next = Node('there')
n.next.next = Node('how')
n.next.next.next = Node('are')
n.next.next.next.next = Node('you')

pprint(n)
