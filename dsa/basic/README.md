# Notes on: Data Structures and Algorithms

## Big O

### Objects

- Object.keys - O(N)
- Object.values - O(N)
- Object.entries - O(N)
- hasOwnProperty - O(1)

### Arrays
- Insertion and Removal
  - Push/Pop (at end) - O(1)
  - Shift/Unshift (at start) - O(N)
  - Concat/Slice/Splice - O(N)
- Sort - O(N * log N)
- Searching - O(N)
  - `indexOf`
- Access - O(1)

## Stacks vs. Queues

**Stacks** follow a *LIFO* or *last-in-first-out* structure.
  - The last thing you put in is the first thing you get out.
  - For example, think of a deck of `cards` or a stack of `plates`.

**Queues** follow a *FIFO* or *first-in-first-out* structure.
  - The first thing you put in is the first thing you get out.
  - For example, think of a deck of `cards` or a stack of `plates`.
