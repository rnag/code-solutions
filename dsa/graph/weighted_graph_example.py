"""
Copy this container_with_water and create a new example file from it as needed

"""
from pprint import pprint

from dsa.graph.weighted_graph import WeightedGraph


graph = WeightedGraph()


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

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "E", 3)
    graph.add_edge("C", "D", 2)
    graph.add_edge("C", "F", 4)
    graph.add_edge("D", "E", 3)
    graph.add_edge("D", "F", 1)
    graph.add_edge("E", "F", 1)

    pprint(graph)
    print()

    result = graph.Djikstra("A", "E")
    print(result)


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
