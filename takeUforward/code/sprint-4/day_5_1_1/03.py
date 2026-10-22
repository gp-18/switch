# Maximum Subarray Sum with Length at Least K
# Given an integer array nums and an integer k, find the maximum sum of a contiguous
# subarray that has a length of at least k.
#
# Example 1:
# Input:  nums = [-4, -2, 1, -3], k = 2
# Output: -1
# Explanation: Subarray [-2, 1] has length 2 and maximum sum = -1.
#
# Example 2:
# Input:  nums = [1, 1, 1, 1, 1, 1], k = 3
# Output: 6
# Explanation: Entire array has length 6 (>= 3) and sum = 6.
#
# Example 3 (Edge Case):
# Input:  nums = [-1, 2, 3, -2, 5], k = 2
# Output: 8
# Explanation: Subarray [2, 3, -2, 5] has length 4 (>= 2) with sum = 8.
#
# Think About:
# - Sliding Window of size k + Kadane Prefix:
#   * Compute initial sum of first k elements: window_sum
#   * ans = window_sum, cur_kadane = 0
#   * For i from k to n - 1:
#       - window_sum += nums[i] - nums[i - k]
#       - cur_kadane = max(nums[i - k], cur_kadane + nums[i - k])
#       - ans = max(ans, window_sum, window_sum + cur_kadane)
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

k = int(input("Enter the minimum length k: "))

print(f"Your array has become: {array}, k is: {k} and now doing the operations on it.")

# Write your solution below
