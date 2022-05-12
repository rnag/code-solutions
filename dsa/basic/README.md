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

## BFS vs. DFS

> Should you use BFS or DFS traversal (for graphs or trees) in the below cases?

#### If you know a solution is not far from the root of the tree:

BFS, because it starts searching closest nodes to parent first.

#### If the tree is very deep and solutions are rare: 

BFS (DFS will take too long)

#### If the tree is very wide:

DFS (BFS will need too much memory, since it needs to store it in a queue)

#### If solutions are frequent but located deep in the tree:

DFS

#### Determining whether a path exists between two nodes:

DFS

#### Finding the shortest path:

BFS
