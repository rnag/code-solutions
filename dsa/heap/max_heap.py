"""
Copy this template and create a new example file from it as needed

"""
from __future__ import annotations

from typing import Any

from dsa.binary_tree.bst import Node
from dataclasses import dataclass, field


@dataclass
class MaxBinaryHeap:
    values: list[Any] = field(default_factory=list)

    def insert(self, element):
        self.values.append(element)
        self.bubble_up()

    def bubble_up(self):
        idx = len(self.values) - 1
        element = self.values[idx]

        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = self.values[parent_idx]

            if element <= parent:
                break

            self.values[parent_idx] = element
            self.values[idx] = parent

            idx = parent_idx

    def extract_max(self) -> Any | None:
        max = self.values[0]
        end = self.values.pop()

        if self.values:
            self.values[0] = end
            self.sink_down()

        return max

    def sink_down(self):
        idx = 0
        ln = len(self.values)
        element = self.values[0]

        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            swap = None

            if left_child_idx < ln:
                left_child = self.values[left_child_idx]
                if left_child > element:
                    swap = left_child_idx

            if right_child_idx < ln:
                right_child = self.values[right_child_idx]
                if (swap is None and right_child > element) \
                        or (swap is not None and right_child > left_child):
                    swap = right_child_idx

            if swap is None:
                break

            self.values[idx] = self.values[swap]
            self.values[swap] = element

            idx = swap
