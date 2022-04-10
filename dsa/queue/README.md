# Queues

Queues are a **FIFO** data structure where the first value added
is always the first one out.

## Examples

- Think about the last time you **waited in line**...
- How about **player queues** for joining online games?
- **Background tasks** on your computer, when uploading or downloading a file.
- **Printing/task processing**, such as *print queues* which
  a printer uses to keep track of what to print.

## Big O

- **Insertion - O(1)**
  - `enqueue` is very fast, it takes constant time
    - We add items to the end of queue, same as with `push` in linked lists.
- **Removal - O(1)**
  - From *start* with `dequeue` is constant time or **O(1)**, because we just move `first` over.
    - We remove items to the start of stack, same as with `shift` in linked lists.
- Searching - **O(N)**
  - Same as a *linked list*
- Access - **O(N)**
  - Same as a *linked list*
