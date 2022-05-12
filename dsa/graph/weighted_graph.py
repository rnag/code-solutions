from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar, Any

from heap.priority_queue import PriorityQueue


T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    vertex: T
    weight: int


@dataclass
class WeightedGraph(Generic[T]):
    adjacency_list: dict[T, list[Node]] = field(default_factory=dict)

    def add_vertex(self, vertex: T):
        """Insert a new vertex in the weighted Graph"""
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1: T, v2: T, weight: int):
        """Insert a new edge in the weighted Graph"""
        self.adjacency_list[v1].append(Node(v2, weight))
        self.adjacency_list[v2].append(Node(v1, weight))

    def Djikstra(self, start: T, finish: T):
        nodes = PriorityQueue()
        distances = {}
        previous = {}
        path = []  # to return at end

        # build up initial state
        for vertex in self.adjacency_list:
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = float('inf')
                nodes.enqueue(vertex, float('inf'))

            previous[vertex] = None

        # as long as there's something to visit
        while nodes.values:
            smallest = nodes.dequeue().val

            if smallest == finish:
                # we are done
                # BUILD UP PATH TO RETURN AT END
                while previous[smallest]:
                    path.append(smallest)
                    smallest = previous[smallest]

                break

            if smallest or distances[smallest] != float('inf'):
                for next_node in self.adjacency_list[smallest]:

                    # find neighboring node
                    # next_node = self.adjacency_list[smallest][neighbor]
                    # print(next_node)
                    # calculate new distance to neighboring node
                    next_neighbor = next_node.vertex
                    candidate = distances[smallest] + next_node.weight

                    if candidate < distances[next_neighbor]:
                        # updating new smallest distance to neighbor
                        distances[next_neighbor] = candidate
                        # updating previous - how we got to neighbor
                        previous[next_neighbor] = smallest
                        # enqueue in priority queue with new priority
                        nodes.enqueue(next_neighbor, candidate)

        path.append(smallest)
        path.reverse()

        return path
