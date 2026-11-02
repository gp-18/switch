# Search X in Sorted Array (Binary Search)
# Given a sorted array of integers nums with 0-based indexing, find the index
# of a specified target integer. Return -1 if the target is not found.
#
# Example 1:
# Input:  nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
#
# Example 2:
# Input:  nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1
#
# Example 3:
# Input:  nums = [-1, 0, 3, 5, 9, 12], target = -1
# Output: 0
#
# Think About:
# - Search space: low = 0, high = len(nums) - 1.
# - Calculate mid = low + (high - low) // 2.
# - If nums[mid] == target: return mid.
# - If nums[mid] < target: search right half (low = mid + 1).
# - If nums[mid] > target: search left half (high = mid - 1).
# - If low > high: target is not present, return -1.
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter the target integer to search : "))

print(f"Your sorted array : {array} with target = {target}")

# Write your solution below:
# Optimal Approach: Iterative Binary Search
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
found_index = -1

while low <= high:
    mid = low + (high - low) // 2

    if array[mid] == target:
        found_index = mid
        break
    elif array[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if found_index == -1:
    print(f"Target {target} is not present in the array (returned -1).")
else:
    print(f"Target {target} is found at index : {found_index}")
