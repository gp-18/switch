# Reverse an Array
# Given an array of integers nums, reverse the array in-place so that
# the first element becomes the last and the last becomes the first.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
#
# Example 2:
# Input:  nums = [10, 20]
# Output: [20, 10]
#
# Example 3 (Edge Case):
# Input:  nums = [7]
# Output: [7]  # A single element remains unchanged
#
# Think About:
# - Put left finger at start (left = 0) and right finger at end (right = len(nums) - 1).
# - Swap nums[left] and nums[right].
# - Move left += 1 and right -= 1.
# - Keep swapping until left >= right.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

