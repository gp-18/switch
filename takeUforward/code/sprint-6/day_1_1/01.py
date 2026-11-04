# Count Occurrences in a Sorted Array
# Given a sorted array of integers arr and an integer target,
# determine how many times target appears in arr.
#
# Example 1:
# Input:  arr = [0, 0, 1, 1, 1, 2, 3], target = 1
# Output: 3
# Explanation: 1 appears 3 times (indices 2, 3, 4).
#
# Example 2:
# Input:  arr = [5, 5, 5, 5, 5, 5], target = 5
# Output: 6
#
# Example 3:
# Input:  arr = [2, 4, 6, 8, 10], target = 3
# Output: 0
#
# Think About:
# - Sorted array contiguity: All occurrences of target form a contiguous subarray [first..last].
# - Run binary search to find the first occurrence (search left when match found).
# - Early exit: If first occurrence is -1, target is absent, return 0.
# - Run binary search to find the last occurrence (search right when match found).
# - Total count = last - first + 1.
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

def find_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    first = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            first = mid
            # Search further left for an earlier index
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def find_last_occurrence(arr, target):
    low = 0
    high = len(arr) - 1
    last = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            last = mid
            # Search further right for a later index
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

first_idx = find_first_occurrence(array, target)

if first_idx == -1:
    count = 0
else:
    last_idx = find_last_occurrence(array, target)
    count = last_idx - first_idx + 1

print(f"The number of occurrences of {target} in the array is : {count}")
