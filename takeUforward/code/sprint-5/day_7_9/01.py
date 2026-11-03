# Single Element in a Sorted Array
# Given an array nums sorted in non-decreasing order. Every number appears twice
# except for one element which appears once. Find the single number in the array.
#
# Example 1:
# Input:  nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# Output: 4
#
# Example 2:
# Input:  nums = [1, 1, 3, 5, 5]
# Output: 3
#
# Example 3:
# Input:  nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]
# Output: 7
#
# Think About:
# - Pairs before single element have indices (even, odd).
# - Pairs after single element have indices (odd, even).
# - Boundary cases: check if nums[0] or nums[n-1] is the single element first.
# - Search interior: low = 1, high = n - 2.
# - If nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]: return nums[mid].
# - XOR trick: mid ^ 1 gives partner index. If nums[mid] == nums[mid ^ 1]: search right (low = mid + 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your sorted array : {array}")

# Write your solution below:
# Optimal Approach: Binary Search using Index Parity
# Time Complexity: O(log N) | Space Complexity: O(1)

def find_single_element(nums, n):
    # Edge case: single element array
    if n == 1:
        return nums[0]

    # Boundary checks:
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    # Search in interior range [1, n - 2]
    low = 1
    high = n - 2

    while low <= high:
        mid = low + (high - low) // 2

        # Check if mid is the unique element
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]

        # Check if we are in the left half:
        # Expected pair index for mid is mid ^ 1
        if nums[mid] == nums[mid ^ 1]:
            # In left half, move right
            low = mid + 1
        else:
            # In right half, move left
            high = mid - 1

    return -1

ans = find_single_element(array, length)
print(f"The single element in the array is : {ans}")
