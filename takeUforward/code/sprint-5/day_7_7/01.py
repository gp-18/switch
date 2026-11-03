# Find Minimum in Rotated Sorted Array
# Given an integer array nums of size n, sorted in ascending order with distinct values,
# rotated an unknown number of times. Find the minimum element in the array.
#
# Example 1:
# Input:  nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 0
#
# Example 2:
# Input:  nums = [3, 4, 5, 1, 2]
# Output: 1
#
# Example 3:
# Input:  nums = [4, 5, 6, 7, -7, 1, 2, 3]
# Output: -7
#
# Think About:
# - If nums[low] <= nums[high]: the entire range is already sorted; ans = min(ans, nums[low]); break.
# - If left half is sorted (nums[low] <= nums[mid]):
#     ans = min(ans, nums[low]), search right half (low = mid + 1).
# - Else right half is sorted:
#     ans = min(ans, nums[mid]), search left half (high = mid - 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the rotated array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your rotated sorted array : {array}")

# Write your solution below:
# Optimal Approach: Binary Search for Inflection Point
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
min_val = float('inf')

while low <= high:
    # If the remaining search space is already sorted:
    if array[low] <= array[high]:
        min_val = min(min_val, array[low])
        break

    mid = low + (high - low) // 2

    # If the left half is sorted:
    if array[low] <= array[mid]:
        min_val = min(min_val, array[low])
        # Eliminate left half, search right
        low = mid + 1
    # If the right half is sorted:
    else:
        min_val = min(min_val, array[mid])
        # Eliminate right half, search left
        high = mid - 1

print(f"The minimum element in the rotated array is : {min_val}")
