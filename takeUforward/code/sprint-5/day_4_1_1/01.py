# Maximum Subarray Sum (Kadane's Algorithm)
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum, and return that sum.
#
# Example 1:
# Input:  nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: Subarray [4, -1, 2, 1] has the largest sum = 6.
#
# Example 2:
# Input:  nums = [1]
# Output: 1
#
# Example 3:
# Input:  nums = [5, 4, -1, 7, 8]
# Output: 23
# Explanation: Entire array has sum = 23.
#
# Think About:
# - Maintain a running current_sum and max_sum (initialized to -infinity or nums[0]).
# - Add current element to current_sum.
# - Update max_sum = max(max_sum, current_sum).
# - If current_sum drops below 0, reset current_sum = 0 (a negative running sum can never help any future subarray).
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

