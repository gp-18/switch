# Majority Element-II (> n/3)
# Given an integer array nums of size n, find all elements that appear strictly
# more than n // 3 times. Return the answer in any order.
#
# Example 1:
# Input:  nums = [3, 2, 3]
# Output: [3]
#
# Example 2:
# Input:  nums = [1, 2]
# Output: [1, 2]
#
# Think About:
# - Maintain two candidates and two counters.
# - Triplet cancellation: decrement both counters when a number differs from both candidates.
# - Run a second verification pass.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:
