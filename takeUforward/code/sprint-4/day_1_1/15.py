# Find Pair with Target Difference in Sorted Array
# Given an array of integers nums sorted in ascending order and a positive integer diff,
# return True if there exists a pair of distinct indices (i, j) such that
# nums[j] - nums[i] == diff, otherwise return False.
#
# Example 1:
# Input:  nums = [1, 2, 4, 7, 10], diff = 3
# Output: True  # (4 - 1 = 3, or 7 - 4 = 3, or 10 - 7 = 3)
#
# Example 2:
# Input:  nums = [2, 3, 5, 8], diff = 4
# Output: False
#
# Example 3 (Edge Case):
# Input:  nums = [1, 5, 5, 9], diff = 0
# Output: True  # (5 - 5 = 0 using indices 1 and 2)
#
# Think About:
# - Both pointers start at front: i = 0 and j = 1.
# - While i < len(nums) and j < len(nums):
#   * If i != j and nums[j] - nums[i] == diff: return True.
#   * If nums[j] - nums[i] < diff: diff is too small, j += 1.
#   * If nums[j] - nums[i] > diff: diff is too big, i += 1.
#   * If i == j: make sure j stays ahead by j += 1.
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space
#

length = int(input("Enter the length of the sorted array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

diff = int(input("Enter the target difference diff : "))

print(f"Your array has become : {array}, diff is : {diff} and now doing the operations on it.")

# Write your solution below

i = 0
j = 1
found = False

while i < len(array) and j < len(array):
    if i == j:
        j += 1
        continue
    current_diff = array[j] - array[i]
    if current_diff == diff:
        found = True
        break
    elif current_diff < diff:
        j += 1
    else:
        i += 1

print(found)
