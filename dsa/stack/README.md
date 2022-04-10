# Stacks

Stacks are a **LIFO** data structure where the last value added
is always the first one out.

## Big O

- **Insertion - O(1)**
  - `push` is very fast, it takes constant time
    - We add items to the start of stack, same as with `unshift` in linked lists.
- **Removal - O(1)**
  - From *start* with `pop` is constant time or **O(1)**, because we just move `first` over.
    - We remove items to the start of stack, same as with `shift` in linked lists.
- Searching - **O(N)**
  - Same as a *linked list*
- Access - **O(N)**
  - Same as a *linked list*
