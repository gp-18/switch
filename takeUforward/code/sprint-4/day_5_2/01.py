# Next Permutation
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
# The next permutation of an array is the next lexicographically greater permutation of its integers.
# If such an arrangement is not possible (array is in descending order), rearrange it to the lowest
# possible order (sorted in ascending order).
# The replacement must be in-place with O(1) extra memory.
#
# Example 1:
# Input:  nums = [1, 2, 3]
# Output: [1, 3, 2]
#
# Example 2:
# Input:  nums = [3, 2, 1]
# Output: [1, 2, 3]  # Edge Case: Last permutation wraps around to lowest
#
# Example 3:
# Input:  nums = [1, 1, 5]
# Output: [1, 5, 1]
#
# Think About:
# - Step 1: Find first index `ind` from right where nums[i] < nums[i + 1].
# - Step 2: If ind == -1, the entire array is in descending order. Reverse it and return.
# - Step 3: Find first element from right that is strictly greater than nums[ind], swap them.
# - Step 4: Reverse the subarray from ind + 1 to end to get the smallest possible suffix.
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i}: "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
