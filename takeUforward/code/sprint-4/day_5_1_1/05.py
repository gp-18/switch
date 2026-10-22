# Maximum Subarray Sum with at Most One Deletion (Google, Meta, Amazon)
# Given an integer array nums, return the maximum sum of a non-empty subarray with at most
# one element deleted. You must choose at least one element.
#
# Example 1:
# Input:  nums = [1, -2, 0, 3]
# Output: 4
# Explanation: Delete -2 to get subarray [1, 0, 3] with sum = 4.
#
# Example 2:
# Input:  nums = [1, -2, -2, 3]
# Output: 3
# Explanation: Subarray [3] gives sum = 3 (no deletion needed).
#
# Example 3 (Edge Case):
# Input:  nums = [-1, -1, -1, -1]
# Output: -1
# Explanation: All negative; maximum single element is -1.
#
# Think About:
# - Two-State Kadane DP:
#   * no_del = maximum subarray sum ending at current index with 0 deletions (standard Kadane)
#   * one_del = maximum subarray sum ending at current index with 1 deletion
#   * For each element num in nums[1:]:
#       one_del = max(no_del, one_del + num)
#       no_del = max(num, no_del + num)
#       ans = max(ans, no_del, one_del)
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
