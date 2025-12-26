# Stacks
stack = []
stack.append(1)
stack.append(2)
stack.pop()       # removes 2
stack[-1]         # peek

# Queue / Deque

from collections import deque

q = deque()
q.append(1)       # enqueue
q.append(2)
q.popleft()       # dequeue
q[0]              # peek

