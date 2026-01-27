The difference between q.popleft() and q.pop() in Python's collections.deque is:

q.popleft(): Removes and returns the element from the left end (front) of the deque. This is typically used for queue (FIFO) operations.
q.pop(): Removes and returns the element from the right end (back) of the deque. This is typically used for stack (LIFO) operations.
Both operations are O(1) time.

Here’s a quick example:

from collections import deque

q = deque([1, 2, 3, 4])

print(q.popleft())  # Output: 1 (removes from the left/front)
print(q.pop())      # Output: 4 (removes from the right/back)
print(q)            # Output: deque([2, 3])
Summary table:

| Method        | Removes from        | Typical use case |
|---------------|---------------------|------------------|
| `q.popleft()` | Left (front)        | Queue (FIFO)     |
| `q.pop()`     | Right (back)        | Stack (LIFO)     |
