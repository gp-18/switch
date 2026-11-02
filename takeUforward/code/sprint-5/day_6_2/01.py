# Largest Subarray with Sum 0
# Given an integer array arr of size n containing both positive and negative integers.
# Find the length of the longest contiguous subarray with sum equal to 0.
# If no such subarray exists, return 0.
#
# Example 1:
# Input:  arr = [15, -2, 2, -8, 1, 7, 10, 23]
# Output: 5
# Explanation: Subarray [-2, 2, -8, 1, 7] sums to 0, length = 5.
#
# Example 2:
# Input:  arr = [2, 10, 4]
# Output: 0
# Explanation: No zero-sum subarray.
#
# Example 3:
# Input:  arr = [1, 0, -4, 3, 1, 0]
# Output: 5
# Explanation: Subarray [0, -4, 3, 1, 0] sums to 0, length = 5.
#
# Think About:
# - If cumulative sum at index i equals cumulative sum at index j (i < j),
#   the sum of elements from i + 1 to j must be 0!
# - If cumulative sum reaches 0 at index i, the subarray from 0 to i has length i + 1.
# - Store only the first occurrence of each cumulative sum in a hash map to maximize subarray length.
# - Time Complexity: O(N)
# - Space Complexity: O(N) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:
# Optimal Approach: Prefix Sum with Hash Map
# Time Complexity: O(N) | Space Complexity: O(N)

sum_map = {}
running_sum = 0
max_length = 0

for i in range(length):
    running_sum += array[i]

    # If running sum is 0, subarray from index 0 to i sums to 0
    if running_sum == 0:
        max_length = i + 1
    # If running sum has been seen before, update max_length
    elif running_sum in sum_map:
        max_length = max(max_length, i - sum_map[running_sum])
    else:
        # Record the earliest occurrence of this running sum
        sum_map[running_sum] = i

print(f"The maximum length of a subarray with sum 0 is : {max_length}")
