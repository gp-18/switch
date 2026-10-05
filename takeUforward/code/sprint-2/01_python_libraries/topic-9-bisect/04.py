# Insert values into a sorted list using insort().

# Example 1:
# Input: arr = [1, 3, 5]; bisect.insort(arr, 4)
# Output: arr -> [1, 3, 4, 5]

# Example 2:
# Input: arr = [10, 30]; bisect.insort(arr, 20)
# Output: arr -> [10, 20, 30]

import bisect

arr = [1, 3, 5]
bisect.insort(arr, 4)
print(f"arr: {arr}")
