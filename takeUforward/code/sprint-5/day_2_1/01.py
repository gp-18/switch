# Find the Repeating and Missing Number
# Given an integer array nums of size n containing values from [1, n] and each value
# appears exactly once in the array, except for A, which appears twice and B which is missing.
# Return the values A and B, as an array of size 2, where A appears at index 0 and B at index 1.
# Note: You are not allowed to modify the original array.
#
# Example 1:
# Input:  nums = [3, 5, 4, 1, 1]
# Output: [1, 2]
# Explanation: 1 appears two times and 2 is missing.
#
# Example 2:
# Input:  nums = [1, 2, 3, 6, 7, 5, 7]
# Output: [7, 4]
# Explanation: 7 appears two times and 4 is missing.
#
# Think About:
# - Mathematical Approach:
#   * S - Sn = X - Y
#   * S2 - S2n = X^2 - Y^2 = (X - Y)(X + Y)
#   * X + Y = (S2 - S2n) // (X - Y)
#   * X = ((X - Y) + (X + Y)) // 2
#   * Y = X - (X - Y)
# - Time Complexity: O(N)
# - Space Complexity: O(1) auxiliary space (array is not modified)
#

length = int(input("Enter the length of the array : "))
array = []

for i in range(length):
    value = int(input(f"Enter the value to insert at index {i} : "))
    array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

# Write your solution below:

# Optimal Approach: Mathematical Linear Equations
# Time Complexity: O(N) | Space Complexity: O(1)

n = len(array)

# Sum and Sum of squares of first n natural numbers
Sn = (n * (n + 1)) // 2
S2n = (n * (n + 1) * (2 * n + 1)) // 6

# Actual sum and sum of squares of array elements
S = 0
S2 = 0
for num in array:
    S += num
    S2 += num * num

# S - Sn = X - Y (val1)
val1 = S - Sn

# S2 - S2n = X^2 - Y^2
val2 = S2 - S2n

# X + Y = (X^2 - Y^2) // (X - Y)
val2 = val2 // val1

# X = ((X + Y) + (X - Y)) // 2
x = (val1 + val2) // 2

# Y = X - (X - Y)
y = x - val1

result = [int(x), int(y)]
print(f"The repeating and missing numbers are: {result}")
