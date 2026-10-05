# Repeatedly pop values from a heap and verify that they come out in priority order.

# Example 1:
# Input: heap = [1, 2, 8, 5, 3] (heapified)
# Output: Pops: 1, 2, 3, 5, 8 (ascending order)

# Example 2:
# Input: heap = [10, 20, 15] (heapified)
# Output: Pops: 10, 15, 20

import heapq

heap = [1, 2, 8, 5, 3]
heapq.heapify(heap)

popped = []
while heap:
    popped.append(heapq.heappop(heap))

print(f"Pops: {popped}")
