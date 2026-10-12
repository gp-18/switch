# Largest Element
# Given an array nums of N integers, find and return the largest element in the array.
#
# Example 1:
# Input:  nums = [2, 5, 1, 3, 0]
# Output: 5
#
# Example 2:
# Input:  nums = [8, 10, 5, 7, 9]
# Output: 10
#
# Think About:
# - Initialize max_val = nums[0].
# - Iterate through nums from index 1 to N - 1: if nums[i] > max_val, update max_val = nums[i].
# - Avoid sorting the array (O(N log N)); a single pass runs in O(N) time.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

