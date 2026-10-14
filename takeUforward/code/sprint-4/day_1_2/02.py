# Check if Array is a Palindrome
# Given an array of integers nums, determine if the array reads the same forward and backward.
# Return True if it is a palindrome, otherwise return False.
#
# Example 1:
# Input:  nums = [1, 2, 3, 2, 1]
# Output: True
#
# Example 2:
# Input:  nums = [1, 2, 3, 4]
# Output: False
#
# Example 3 (Edge Case):
# Input:  nums = [5]
# Output: True  # Single element is always a palindrome
#
# Think About:
# - Place left = 0 and right = len(nums) - 1.
# - Compare nums[left] and nums[right]:
#   * If not equal, return False immediately.
#   * If equal, move inward: left += 1, right -= 1.
# - If pointers cross without mismatch, return True.
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

reverse_array = list(reversed(array))

if array == reverse_array:
    print("True")
else:
    print("False")