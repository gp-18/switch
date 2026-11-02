# Search Insert Position
# Given a sorted array of distinct integers nums and a target value,
# return the index if the target is found. If not, return the index
# where it would be if it were inserted in order.
#
# Example 1:
# Input:  nums = [1, 3, 5, 6], target = 5
# Output: 2
#
# Example 2:
# Input:  nums = [1, 3, 5, 6], target = 2
# Output: 1
#
# Example 3:
# Input:  nums = [1, 3, 5, 6], target = 7
# Output: 4
#
# Think About:
# - Search Insert Position is mathematically identical to Lower Bound (smallest index where nums[i] >= target).
# - If target is present: returns exact index.
# - If target is absent: returns the first element greater than target (the insertion point).
# - If target > all elements: returns len(nums).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

target = int(input("Enter target value to search/insert : "))

print(f"Your sorted array : {array} with target = {target}")

# Write your solution below:
# Optimal Approach: Binary Search (Lower Bound)
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
ans = length

while low <= high:
    mid = low + (high - low) // 2

    if array[mid] >= target:
        ans = mid
        # Search left half for a smaller index
        high = mid - 1
    else:
        # Search right half
        low = mid + 1

print(f"The search insert position of {target} is : {ans}")
