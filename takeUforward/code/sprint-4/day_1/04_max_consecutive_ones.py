# Maximum Consecutive Ones
# Given a binary array nums containing only 0s and 1s, return the maximum number of consecutive 1s present in the array.
#
# Example 1:
# Input:  nums = [1, 1, 0, 1, 1, 1]
# Output: 3
#
# Example 2:
# Input:  nums = [1, 0, 1, 1, 0, 1]
# Output: 2
#
# Think About:
# - Maintain a current streak count cnt = 0 and a maximum count max_cnt = 0.
# - Iterate through the array:
#   * If num == 1: increment cnt += 1 and update max_cnt = max(max_cnt, cnt).
#   * If num == 0: reset cnt = 0.
# - Time Complexity: O(N)
# - Space Complexity: O(1)
#

length = int(input("Enter the length of the binary array : "))
array = []

for i in range(length):
    value = int(input(f"Enter binary value (0 or 1) at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below

