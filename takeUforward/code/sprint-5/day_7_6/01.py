# Search in Rotated Sorted Array-II (With Duplicates)
# Given an integer array nums, sorted in ascending order (may contain duplicate values)
# and a target value k. The array is rotated at some unknown pivot point.
# Return True if k is present, and False otherwise.
#
# Example 1:
# Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3
# Output: True
#
# Example 2:
# Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 10
# Output: False
#
# Example 3:
# Input:  nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 7
# Output: True
#
# Think About:
# - When nums[low] == nums[mid] == nums[high], we cannot determine which half is sorted.
# - Shrink search space by low += 1, high -= 1 and continue.
# - Otherwise, determine which half is sorted and narrow search space as in Rotated Array-I.
# - Time Complexity: O(log N) average, O(N/2) worst case when all elements are duplicates.
# - Space Complexity: O(1) auxiliary space.
#

length = int(input("Enter the length of the rotated array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

k = int(input("Enter target value k : "))

print(f"Your rotated array (with duplicates) : {array} with target k = {k}")

# Write your solution below:
# Optimal Approach: Binary Search with Duplicate Boundary Shrinking
# Time Complexity: O(log N) avg, O(N) worst | Space Complexity: O(1)

low = 0
high = length - 1
is_present = False

while low <= high:
    mid = low + (high - low) // 2

    if array[mid] == k:
        is_present = True
        break

    # When duplicates prevent determining which half is sorted
    if array[low] == array[mid] == array[high]:
        low += 1
        high -= 1
        continue

    # Check if the left half is sorted
    if array[low] <= array[mid]:
        if array[low] <= k <= array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    # Right half is sorted
    else:
        if array[mid] <= k <= array[high]:
            low = mid + 1
        else:
            high = mid - 1

if is_present:
    print(f"Target {k} is present in the array (True).")
else:
    print(f"Target {k} is NOT present in the array (False).")
