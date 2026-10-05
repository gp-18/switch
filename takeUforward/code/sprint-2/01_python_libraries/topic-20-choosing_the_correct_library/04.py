# You need to find where a value should be inserted into a sorted list. Which library would you choose?

# Example 1:
# Input: Requirement: Binary search insertion point in sorted list
# Output: bisect (bisect_left() or bisect_right() in O(log n) time)

# Example 2:
# Input: sorted_list = [10, 20, 30], target = 25
# Output: bisect.bisect_left(sorted_list, 25) -> index 2

import bisect

# Answer: bisect (bisect_left or bisect_right)
# Binary search insertion position in O(log n) time.
sorted_list = [10, 20, 30]
target = 25
print(f"Insertion index: {bisect.bisect_left(sorted_list, target)}")
