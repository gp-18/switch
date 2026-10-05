# Implement a max-heap for integers using the negative-value technique.

# Example 1:
# Input: Push 5, 1, 10 as -5, -1, -10
# Output: -heappop() returns 10, then 5, then 1 (max-heap order)

# Example 2:
# Input: Push 3, 9, 2 as -3, -9, -2
# Output: Pops: 9, 3, 2

import heapq

max_heap = []
for val in [5, 1, 10]:
    heapq.heappush(max_heap, -val)

popped_max = []
while max_heap:
    popped_max.append(-heapq.heappop(max_heap))

print(f"Max-heap order: {popped_max}")
