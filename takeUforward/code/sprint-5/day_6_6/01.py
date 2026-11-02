# Lower Bound in a Sorted Array
# Given a sorted array nums of size n and an integer x, find the lower bound of x.
# The lower bound algorithm finds the first and smallest index in a sorted array
# where the value at that index is greater than or equal to x (nums[index] >= x).
# If no such index is found, return the size of the array n.
#
# Example 1:
# Input:  nums = [1, 2, 2, 3], x = 2
# Output: 1
# Explanation: nums[1] = 2 >= 2.
#
# Example 2:
# Input:  nums = [3, 5, 8, 15, 19], x = 9
# Output: 3
# Explanation: nums[3] = 15 >= 9.
#
# Example 3:
# Input:  nums = [3, 5, 8, 15, 19], x = 3
# Output: 0
# Explanation: nums[0] = 3 >= 3.
#
# Think About:
# - Initialize ans = len(nums).
# - If nums[mid] >= x: ans = mid, search left (high = mid - 1) to find an even smaller index.
# - If nums[mid] < x: search right (low = mid + 1).
# - Time Complexity: O(log N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

x = int(input("Enter key x to find lower bound : "))

print(f"Your sorted array : {array} with key x = {x}")

# Write your solution below:
# Optimal Approach: Binary Search for Lower Bound
# Time Complexity: O(log N) | Space Complexity: O(1)

low = 0
high = length - 1
ans = length

while low <= high:
    mid = low + (high - low) // 2

    if array[mid] >= x:
        ans = mid
        # Look for a smaller index on the left
        high = mid - 1
    else:
        # nums[mid] is too small, search right
        low = mid + 1

print(f"The lower bound of {x} is at index : {ans}")
