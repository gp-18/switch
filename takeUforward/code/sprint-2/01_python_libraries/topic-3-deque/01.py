# Implement a queue using deque with enqueue and dequeue operations.

# Example 1:
# Input: enqueue(10), enqueue(20), dequeue()
# Output: Dequeued: 10, Remaining: deque([20])

# Example 2:
# Input: enqueue('A'), dequeue()
# Output: Dequeued: 'A', Remaining: deque([])

from collections import deque

queue = deque()

def enqueue(val):
    queue.append(val)

def dequeue():
    return queue.popleft() if queue else None

enqueue(10)
enqueue(20)
val = dequeue()
print(f"Dequeued: {val}, Remaining: {queue}")
