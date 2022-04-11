from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar


T = TypeVar('T')


@dataclass
class Graph(Generic[T]):
    adjacency_list: dict[T, list[T]] = field(default_factory=dict)

    def add_vertex(self, vertex: T):
        """Insert a new vertex in the Graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1: T, v2: T):
        """Insert a new edge in the Graph"""
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def remove_edge(self, v1: T, v2: T):
        """Remove an existing edge in the Graph"""
        self.adjacency_list[v1].remove(v2)
        self.adjacency_list[v2].remove(v1)

    def remove_vertex(self, vertex: T):
        """Remove an existing vertex in the Graph"""
        for adjacent_vertex in self.adjacency_list[vertex]:
            self.remove_edge(vertex, adjacent_vertex)

        del self.adjacency_list[vertex]

    def BFS(self, start: T):
        """breadth-first search (HORIZONTAL before VERTICAL)"""
        queue = [start]
        result = []
        visited = {start: True}

        while queue:
            # remove from start
            current_vertex = queue.pop(0)
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def DFS_recursive(self, start: T):
        """depth-first search (VERTICAL before HORIZONTAL)"""
        result = []
        visited = {}

        def dfs(vertex: T):
            if not vertex:
                return None

            visited[vertex] = True
            result.append(vertex)

            for neighbor in self.adjacency_list[vertex]:

                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)

        return result

    def DFS_iterative(self, start: T):
        """depth-first search (VERTICAL before HORIZONTAL)"""
        stack = [start]
        result = []
        visited = {start: True}

        while stack:
            current_vertex = stack.pop()
            result.append(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return result
