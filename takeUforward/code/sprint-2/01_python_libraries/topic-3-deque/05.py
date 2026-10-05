# Demonstrate appendleft(), popleft(), append(), and pop() and explain why deque is useful for queues.

# Example 1:
# Input: d = deque(); d.append(1); d.appendleft(2); d.pop(); d.popleft()
# Output: All operations run in O(1) time without list memory-shift overhead

# Example 2:
# Input: d = deque([10, 20]); d.appendleft(5); d.append(30)
# Output: deque([5, 10, 20, 30])

from collections import deque

d = deque([10, 20])
d.appendleft(5)
d.append(30)
print(f"After appendleft(5) and append(30): {d}")

popped_left = d.popleft()
popped_right = d.pop()
print(f"popleft(): {popped_left}, pop(): {popped_right}, remaining: {d}")
