# First and Last Occurrence in a Sorted Array
# Given an array of integers nums sorted in non-decreasing order,
# find the starting and ending position of a given target value.
# If target is not found, return [-1, -1].
#
# Example 1:
# Input:  nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
#
# Example 2:
# Input:  nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
#
# Example 3:
# Input:  nums = [5, 7, 7, 8, 8, 10], target = 5
# Output: [0, 0]
#
# Think About:
# - First Occurrence: When nums[mid] == target, record first = mid and search left (high = mid - 1).
# - Last Occurrence: When nums[mid] == target, record last = mid and search right (low = mid + 1).
# - Early Exit: If first == -1, target does not exist -> return [-1, -1] immediately.
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter target value : "))

print(f"Your sorted array : {array} with target = {target}")

# Write your solution below:
# Optimal Approach: Two Binary Searches (First & Last Occurrence)
# Time Complexity: O(log N) | Space Complexity: O(1)

def find_first(nums, target):
    low, high = 0, len(nums) - 1
    first = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            first = mid
            # Continue searching left for an earlier index
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def find_last(nums, target):
    low, high = 0, len(nums) - 1
    last = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            last = mid
            # Continue searching right for a later index
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

first_idx = find_first(array, target)

# Early exit if target is not in the array
if first_idx == -1:
    result = [-1, -1]
else:
    last_idx = find_last(array, target)
    result = [first_idx, last_idx]

print(f"First and last occurrence of {target} : {result}")
if result != [-1, -1]:
    count = result[1] - result[0] + 1
    print(f"Total count of {target} in array : {count}")
