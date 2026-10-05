# Find the k smallest values from a list using a heap.

# Example 1:
# Input: nums = [7, 10, 4, 3, 20, 15], k = 3
# Output: [3, 4, 7]

# Example 2:
# Input: nums = [1, 5, 2, 8, 3], k = 2
# Output: [1, 2]

import heapq

nums = [7, 10, 4, 3, 20, 15]
k = 3
k_smallest = heapq.nsmallest(k, nums)
print(k_smallest)
