# You need to repeatedly retrieve the smallest priority value. Which library would you choose?

# Example 1:
# Input: Requirement: Dynamic stream where min value is repeatedly extracted
# Output: heapq (min-heap provides O(log n) push/pop and O(1) min access)

# Example 2:
# Input: Priority queue implementation
# Output: heapq

import heapq

# Answer: heapq
# Min-heap allows retrieving the smallest priority value in O(1) peek and O(log n) pop.
pq = [30, 10, 20]
heapq.heapify(pq)
print(f"Smallest priority: {heapq.heappop(pq)}")
