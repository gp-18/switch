# Upper Bound in a Sorted Array
# Given a sorted array nums of size n and an integer x, find the upper bound of x.
# The upper bound is defined as the smallest index i such that nums[i] > x.
# If no such index is found, return the size of the array n.
#
# Example 1:
# Input:  nums = [1, 2, 2, 3], x = 2
# Output: 3
# Explanation: nums[3] = 3 > 2.
#
# Example 2:
# Input:  nums = [3, 5, 8, 15, 19], x = 9
# Output: 3
# Explanation: nums[3] = 15 > 9.
#
# Example 3:
# Input:  nums = [3, 5, 8, 15, 19], x = 3
# Output: 1
# Explanation: nums[1] = 5 > 3.
#
# Think About:
# - Initialize low = 0, high = len(nums) - 1, ans = len(nums).
# - If nums[mid] > x:
#     ans = mid, search left (high = mid - 1) to find a smaller index.
# - Else (nums[mid] <= x):
#     search right (low = mid + 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

x = int(input("Enter key x to find upper bound : "))

print(f"Your sorted array : {array} with key x = {x}")

# Write your solution below:
# Optimal Approach: Binary Search for Upper Bound
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
ans = length

while low <= high:
    mid = low + (high - low) // 2

    # Check if mid element is strictly greater than x
    if array[mid] > x:
        ans = mid
        # Search left half for an even smaller index
        high = mid - 1
    else:
        # Otherwise, search right half
        low = mid + 1

print(f"The upper bound of {x} is at index : {ans}")
