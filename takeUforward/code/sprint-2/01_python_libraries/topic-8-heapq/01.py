# Create a min-heap and insert five integers using heappush().

# Example 1:
# Input: heappush(5), heappush(3), heappush(8), heappush(1), heappush(2)
# Output: heap[0] is minimum element: 1

# Example 2:
# Input: heappush(10), heappush(4), heappush(15)
# Output: heap[0] is 4

import heapq

heap = []
for val in [5, 3, 8, 1, 2]:
    heapq.heappush(heap, val)

print(f"heap: {heap}, min element: {heap[0]}")
