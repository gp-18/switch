# Leaders in an Array
# Given an integer array nums, return a list of all the leaders in the array.
# An element is a leader if its value is strictly greater than all elements to its right in the array.
# The rightmost element is always a leader. The leaders must appear in the order they appear in nums.
#
# Example 1:
# Input:  nums = [1, 2, 5, 3, 1, 2]
# Output: [5, 3, 2]
#
# Example 2:
# Input:  nums = [-3, 4, 5, 1, -4, -5]
# Output: [5, 1, -4, -5]
#
# Example 3 (Edge Case):
# Input:  nums = [10]
# Output: [10]  # Single element is always a leader
#
# Think About:
# - Traverse backwards from right to left (index n - 1 down to 0).
# - Maintain max_from_right = -float('inf').
# - If nums[i] > max_from_right:
#     * Append nums[i] to leaders list.
#     * Update max_from_right = nums[i].
# - Reverse the leaders list at the end to restore original left-to-right order.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space (excluding output list)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

# Optimal Approach: Suffix Maximum with Right-to-Left Traversal
# Time Complexity: O(N) | Space Complexity: O(1) auxiliary space
leaders = []
max_from_right = -float('inf')

# Traverse the array backwards from the last element to the first
for i in range(len(array) - 1, -1, -1):
    # An element is a leader if it is strictly greater than all elements to its right
    if array[i] > max_from_right:
        leaders.append(array[i])
        max_from_right = array[i]

# Since leaders were found from right to left, reverse to maintain original relative order
leaders.reverse()

print(f"Leaders in the array : {leaders}")
