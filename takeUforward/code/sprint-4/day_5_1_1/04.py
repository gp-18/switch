# Maximum Sum Circular Subarray (Amazon, Microsoft, Google)
# Given a circular integer array nums of length n, find the maximum possible sum of a
# non-empty subarray. The end of the array wraps around to connect to the beginning.
#
# Example 1:
# Input:  nums = [1, -2, 3, -2]
# Output: 3
# Explanation: Subarray [3] has maximum sum = 3 (no wrap needed).
#
# Example 2:
# Input:  nums = [5, -3, 5]
# Output: 10
# Explanation: Subarray [5, 5] wrapping from index 2 to index 0 gives sum = 10.
#
# Example 3 (Edge Case):
# Input:  nums = [-3, -2, -3]
# Output: -2
# Explanation: All numbers negative; max single element is -2. Circular wrap would give empty subarray.
#
# Think About:
# - Two cases for maximum circular subarray sum:
#   1. Non-wrapping subarray: standard Kadane max_sum.
#   2. Wrapping subarray: total_sum - min_subarray_sum (inverted Kadane min_sum).
# - Edge Case: If all numbers are negative, max_sum < 0. In this case, return max_sum.
# - Otherwise: return max(max_sum, total_sum - min_sum).
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
