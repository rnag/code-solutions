"""
Copy this template and create a new example file from it as needed

"""
from pprint import pprint

from dsa.heap.priority_queue import PriorityQueue


pq = PriorityQueue()


def main():
    global pq
    print('=== Example: `enqueue()` ===')
    pq.enqueue("common cold", 5)
    pq.enqueue("gunshot wound", 1)
    pq.enqueue("high fever", 4)
    pq.enqueue("broken arm", 2)
    pq.enqueue("glass in foot", 3)

    pprint(pq)
    print()

    print('=== Example: `dequeue()` ===')
    for _ in range(len(pq.values)):
        print(pq.dequeue())


if __name__ == '__main__':
    main()
