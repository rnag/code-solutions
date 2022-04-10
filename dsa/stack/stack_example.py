from dsa.stack.stack import Stack

s = Stack()

print('=== Example: `push()` ===')
print('Size:  ', s.push('my FIRST item'))
print('Stack: ', s)
print()
print('Size:  ', s.push('my SECOND item'))
print('Stack: ', s)
print()
print('Size:  ', s.push('my THIRD item'))
print('Stack: ', s)

# assert `size` of stack is as expected
assert s.size == 3

print()

print('=== Example: `pop()` ===')
# last iteration should return an undefined
for i in range(s.size + 1):
    print('Removed: ', s.pop())
    print('Stack:   ', s)
    print()
