"""
Implement the 'weave' function.  Weave
receives two queues as arguments and combines the
contents of each into a new, third queue.
The third queue should contain the *alternating* content
of the two queues.  The function should handle
queues of different lengths without inserting
'undefined' into the new one.

--- Example

   const queue_one = new Queue(1, 2)
   const queue_two = new Queue('Hi', 'There')
   const q = weave(queue_one, queue_two)
   q.dequeue()  # 1
   q.dequeue()  # 'Hi'
   q.dequeue()  # 2
   q.dequeue()  # 'There'
"""
from queue import Queue


def weave(source_one: Queue, source_two: Queue) -> Queue:
    result = Queue()

    while source_one.first or source_two.first:
        if source_one.first:
            result.enqueue(source_one.dequeue())
        if source_two.first:
            result.enqueue(source_two.dequeue())

    return result
