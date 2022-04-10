from dsa.queue.queue import Queue

q = Queue()

print('=== Example: `enqueue()` ===')
print('Size:  ', q.enqueue('my FIRST item'))
print('Queue: ', q)
print()
print('Size:  ', q.enqueue('my SECOND item'))
print('Queue: ', q)
print()
print('Size:  ', q.enqueue('my THIRD item'))
print('Queue: ', q)

# assert `size` of Queue is as expected
assert q.size == 3

print()

print('=== Example: `dequeue()` ===')
# last iteration should return an undefined
for i in range(q.size + 1):
    print('Removed: ', q.dequeue())
    print('Queue:   ', q)
    print()
