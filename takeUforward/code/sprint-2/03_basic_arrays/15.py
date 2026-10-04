# Count Elements Greater Than a Given Number
# Given an array `nums` and a threshold integer `k`, count how many elements are strictly greater than `k`.
#
# Example 1:
# Input: nums = [1, 5, 8, 3, 10, 2], k = 4
# Output: 3  # Elements greater than 4: 5, 8, 10
#
# Example 2:
# Input: nums = [1, 2, 3], k = 5
# Output: 0
#
# Example 3 (Edge Case - Negative Threshold):
# Input: nums = [-10, -5, -1, 0, 2], k = -5
# Output: 3  # Elements greater than -5: -1, 0, 2

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

