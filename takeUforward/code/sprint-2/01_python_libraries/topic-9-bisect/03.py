# Determine how many occurrences of a target exist using bisect_left() and bisect_right().

# Example 1:
# Input: arr = [1, 2, 4, 4, 4, 5, 6], target = 4
# Output: bisect_right(arr, 4) - bisect_left(arr, 4) = 5 - 2 = 3

# Example 2:
# Input: arr = [10, 20, 30], target = 25
# Output: Count = 0

import bisect

arr = [1, 2, 4, 4, 4, 5, 6]
target = 4
count = bisect.bisect_right(arr, target) - bisect.bisect_left(arr, target)
print(f"Count of {target}: {count}")
