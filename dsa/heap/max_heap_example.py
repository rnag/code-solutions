"""
Copy this template and create a new example file from it as needed

"""
from pprint import pprint

from dsa.heap.max_heap import MaxBinaryHeap


heap = MaxBinaryHeap()


def main():
    global heap
    print('=== Example: `insert()` ===')
    heap.insert(10)
    heap.insert(5)
    heap.insert(13)
    heap.insert(11)
    heap.insert(2)
    heap.insert(16)
    heap.insert(16)
    heap.insert(7)

    pprint(heap)
    print()

    print('=== Example: `extract_max()` ===')
    for _ in range(len(heap.values)):
        print(heap.extract_max())


if __name__ == '__main__':
    main()
