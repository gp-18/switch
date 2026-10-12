# Sort Array By Parity (Evens First, Odds Last)
# Given an array of integers nums, rearrange the array in-place so that
# all even integers appear at the beginning and all odd integers appear at the end.
# Any order inside the even and odd groups is acceptable.
#
# Example 1:
# Input:  nums = [3, 1, 2, 4]
# Output: [4, 2, 1, 3]  # (or [2, 4, 3, 1] - any even-then-odd order is valid)
#
# Example 2:
# Input:  nums = [1, 3, 5, 2]
# Output: [2, 3, 5, 1]
#
# Example 3 (Edge Case):
# Input:  nums = [2, 4, 6]
# Output: [2, 4, 6]  # Already all even
#
# Think About:
# - Put left = 0 and right = len(nums) - 1.
# - While nums[left] % 2 == 0: left += 1 (evens stay on left).
# - While nums[right] % 2 != 0: right -= 1 (odds stay on right).
# - When left < right: swap nums[left] and nums[right], advance both.
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

