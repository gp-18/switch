# Search in Rotated Sorted Array-I (Distinct Elements)
# Given an integer array nums, sorted in ascending order (with distinct values)
# and a target value k. The array is rotated at some unknown pivot point.
# Find the index of k if present, else return -1.
#
# Example 1:
# Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 0
# Output: 4
#
# Example 2:
# Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 3
# Output: -1
#
# Example 3:
# Input:  nums = [4, 5, 6, 7, 0, 1, 2], k = 5
# Output: 1
#
# Think About:
# - At any mid, one half (left or right) is guaranteed to be sorted.
# - If left part is sorted (nums[low] <= nums[mid]):
#     Check if nums[low] <= k <= nums[mid] -> high = mid - 1, else low = mid + 1.
# - Else right part is sorted:
#     Check if nums[mid] <= k <= nums[high] -> low = mid + 1, else high = mid - 1.
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the rotated array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter target value k : "))

print(f"Your rotated sorted array : {array} with target k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search using Sorted Half Invariant
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
found_index = -1

while low <= high:
    mid = low + (high - low) // 2

    # Check if mid points to target
    if array[mid] == k:
        found_index = mid
        break

    # Check if the left half is sorted
    if array[low] <= array[mid]:
        # Target exists in the left sorted half
        if array[low] <= k <= array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # Otherwise, the right half is sorted
    else:
        # Target exists in the right sorted half
        if array[mid] <= k <= array[high]:
            low = mid + 1
        else:
            high = mid - 1

if found_index == -1:
    print(f"Target {k} is not present in the array (returned -1).")
else:
    print(f"Target {k} is found at index : {found_index}")
