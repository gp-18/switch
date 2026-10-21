# Segregate 0s and 1s in a Binary Array
# Given a binary array nums consisting only of 0s and 1s, sort the array in-place so that
# all 0s appear on the left and all 1s appear on the right in a single pass with O(1) extra space.
#
# Example 1:
# Input:  nums = [0, 1, 0, 1, 0, 0, 1, 1]
# Output: [0, 0, 0, 0, 1, 1, 1, 1]
#
# Example 2:
# Input:  nums = [1, 1, 0]
# Output: [0, 1, 1]
#
# Example 3 (Edge Case):
# Input:  nums = [0, 0, 0]
# Output: [0, 0, 0]
#
# Think About:
# - Two-Pointer Partition:
#   * left = 0, right = n - 1
#   * While left < right:
#       - Advance left while nums[left] == 0 and left < right
#       - Decrement right while nums[right] == 1 and left < right
#       - If left < right, swap nums[left] and nums[right], left += 1, right -= 1
# - Time Complexity: O(N)
# - Space Complexity: O(1) in-place
#

length = int(input("Enter the length of the array: "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} (0 or 1): "))
    array.append(value)

print(f"Your array has become: {array} and now doing the operations on it.")

# Write your solution below
