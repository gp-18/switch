# Reverse Subarray Between Indices L and R
# Given an array nums and two valid indices L and R where 0 <= L <= R < len(nums),
# reverse only the elements from index L to index R in-place.
# Leave all other elements in their original positions.
#
# Example 1:
# Input:  nums = [1, 2, 3, 4, 5, 6], L = 1, R = 4
# Output: [1, 5, 4, 3, 2, 6]
#
# Example 2:
# Input:  nums = [9, 8, 7, 6], L = 0, R = 2
# Output: [7, 8, 9, 6]
#
# Example 3 (Edge Case):
# Input:  nums = [4, 5, 6], L = 1, R = 1
# Output: [4, 5, 6]  # Subarray of length 1 stays unchanged
#
# Think About:
# - Same logic as reversing an array, but start at left = L and right = R.
# - Swap nums[left] and nums[right], move inward (left += 1, right -= 1).
# - Stop when left >= right.
# - Time Complexity: O(R - L + 1) <= O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

L = int(input("Enter start index L : "))
R = int(input("Enter end index R : "))

print(f"Your array has become : {array}, L = {L}, R = {R} and now doing the operations on it.")

# Write your solution below

