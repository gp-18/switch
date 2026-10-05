# Find the rightmost insertion position of a target with duplicates.

# Example 1:
# Input: arr = [1, 2, 4, 4, 5], target = 4
# Output: bisect_right(arr, 4) -> 4

# Example 2:
# Input: arr = [2, 2, 2], target = 2
# Output: bisect_right(arr, 2) -> 3

import bisect

arr = [1, 2, 4, 4, 5]
target = 4
idx = bisect.bisect_right(arr, target)
print(f"bisect_right index: {idx}")
