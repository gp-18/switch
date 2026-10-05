# You need to remove items from both ends of a queue. Which data structure would you choose and why?

# Example 1:
# Input: Requirement: Fast append and pop from both left and right ends
# Output: collections.deque (O(1) time complexity for operations at both ends)

# Example 2:
# Input: BFS traversal queue or sliding window
# Output: collections.deque

from collections import deque

# Answer: collections.deque
# deque provides O(1) time complexity for appending and popping from both ends.
q = deque([1, 2, 3])
q.appendleft(0)
q.append(4)
q.popleft()
q.pop()
print(f"deque operations: {list(q)}")
