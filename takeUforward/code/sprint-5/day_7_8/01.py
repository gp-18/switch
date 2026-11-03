# Find Out How Many Times the Array is Rotated
# Given an integer array nums of size n, sorted in ascending order with distinct values.
# The array has been right-rotated an unknown number of times.
# Find the number of rotations.
#
# Example 1:
# Input:  nums = [4, 5, 6, 7, 0, 1, 2, 3]
# Output: 4
# Explanation: Minimum element 0 is at index 4, meaning rotated 4 times.
#
# Example 2:
# Input:  nums = [3, 4, 5, 1, 2]
# Output: 3
#
# Example 3:
# Input:  nums = [4, 5, 1, 2]
# Output: 2
#
# Think About:
# - Number of right rotations is precisely the index of the minimum element!
# - Run binary search to find the minimum element and track its index.
# - If nums[low] <= nums[high]: array is sorted, check nums[low] and break.
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
# Optimal Approach: Binary Search for Index of Minimum Element
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
min_val = float('inf')
min_index = -1

while low <= high:
    # If the remaining search space is already sorted:
    if array[low] <= array[high]:
        if array[low] < min_val:
            min_val = array[low]
            min_index = low
        break

    mid = low + (high - low) // 2

    # Check if left half is sorted:
    if array[low] <= array[mid]:
        if array[low] < min_val:
            min_val = array[low]
            min_index = low
        # Eliminate left half, search right
        low = mid + 1
    # Right half is sorted:
    else:
        if array[mid] < min_val:
            min_val = array[mid]
            min_index = mid
        # Eliminate right half, search left
        high = mid - 1

print(f"The minimum element is {min_val} at index {min_index}.")
print(f"The array has been rotated {min_index} times.")
