## Singly Linked List

### Big O

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
