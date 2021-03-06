## Singly Linked List

### Big O

>  Wrap up: singly-linked lists beat out arrays at *insertion* and *removal*.

- **Insertion - O(1)**
  - `push` and `unshift` are very fast, they take constant time
  - In arrays, this is *not* the case. It is O(N) instead.
- **Removal - O(1) or O(N)**
  - From *start* with `shift` is constant time or **O(1)**, because we just move `head` over.
  - From *end* with `pop` is **O(N)**, because we have to traverse using `next` all the way from the start, or `head`.
- **Searching - O(N)**
  - Where `N` is the length of the list, so worst case is **O(N)** assuming that the item we want
    is closer to the end of the linked list.
- **Access - O(N)**
  - Same note as for *Searching* above.

## Doubly Linked List

Almost identical to Singly Linked lists, except *every* node
has **another** pointer, to the `previous` node.

### Big O

>  Wrap up: doubly-linked lists beat out singly-linked lists at *removal*.

- **Insertion - O(1)**
  - `push` and `unshift` are very fast, they take constant time
  - In arrays, this is *not* the case. It is O(N) instead.
- **Removal - O(1)**
  - From *start* with `shift` is constant time or **O(1)**, because we just move `head` over.
  - From *end* with `pop` is constant time, because we can just access `prev` of the `tail`, or last node.
- **Searching - O(N)** 
  - Where `N` is the length of the list, so worst case is **O(N)** assuming that the item we want
    is closer to the end of the linked list.
  - Technically searching is **O(N/2)**, but that still simplifies to **O(N)**.
- **Access - O(N)**
  - Same note as for *Searching* above.
