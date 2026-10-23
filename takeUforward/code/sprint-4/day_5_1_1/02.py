# Maximum Absolute Subarray Sum
# Given an integer array nums, find the maximum absolute sum of any contiguous subarray.
# The absolute sum of a subarray [nums[l], ..., nums[r]] is |nums[l] + ... + nums[r]|.
#
# Example 1:
# Input:  nums = [1, -3, 2, 3, -4]
# Output: 5
# Explanation: Subarray [2, 3] has sum 5, absolute sum = 5.
#
# Example 2:
# Input:  nums = [2, -5, 1, -4, 3, -2]
# Output: 8
# Explanation: Subarray [-5, 1, -4] has sum -8, absolute sum = 8.
#
# Example 3 (Edge Case):
# Input:  nums = [-10]
# Output: 10
# Explanation: Single element has absolute sum = 10.
#
# Think About:
# - Track both maximum subarray sum and minimum subarray sum:
#   * max_sum = max contiguous sum (standard Kadane)
#   * min_sum = min contiguous sum (inverted Kadane)
#   * Result is max(max_sum, abs(min_sum))
# - Can be done in a single loop tracking cur_max and cur_min.
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
max_sum = float("-inf")
min_sum = float("inf")

cur_max = 0
cur_min = 0

for i in range(len(array)):
    # Normal Kadane: find maximum subarray sum
    cur_max += array[i]
    max_sum = max(max_sum, cur_max)

    if cur_max < 0:
        cur_max = 0

    # Inverted Kadane: find minimum subarray sum
    cur_min += array[i]
    min_sum = min(min_sum, cur_min)

    if cur_min > 0:
        cur_min = 0

# Choose the larger absolute sum
answer = max(max_sum, abs(min_sum))

print(f"Maximum absolute subarray sum: {answer}")
