"""
Copy this template and create a new example file from it as needed

"""
from pprint import pprint

from dsa.graph.graph import Graph


graph = Graph()


def main():
    example_2()


def example_2():
    global graph
    print('=== Example: `add_vertex()` ===')
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "E")
    graph.add_edge("D", "E")
    graph.add_edge("D", "F")
    graph.add_edge("E", "F")

    pprint(graph)

    result = graph.DFS_recursive("A")
    assert result == ['A', 'B', 'D', 'E', 'C', 'F']

    result = graph.DFS_iterative("A")
    assert result == ['A', 'C', 'E', 'F', 'D', 'B']

    result = graph.BFS("A")
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']


def example_1():
    global graph
    print('=== Example: `add_vertex()` ===')
    graph.add_vertex("Dallas")
    graph.add_vertex("Tokyo")
    graph.add_vertex("Aspen")

    graph.add_edge("Dallas", "Tokyo")
    graph.add_edge("Dallas", "Aspen")

    pprint(graph)
    print()

    graph.remove_edge("Tokyo", "Dallas")

    pprint(graph)
    print()


def traverse_method(meth_name: str):
    print(f'=== Example: `{meth_name}()` ===')
    meth = getattr(graph, meth_name)
    result = meth()
    print(result)
    print()

    return result


if __name__ == '__main__':
    main()
