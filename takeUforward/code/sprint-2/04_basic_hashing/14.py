# Count Pairs with Equal Elements
# Given an array `nums`, count and return the number of pairs (i, j) such that i < j and nums[i] == nums[j].
#
# Example 1:
# Input: nums = [1, 2, 3, 1, 1, 3]
# Output: 4  # Pairs: (0,3), (0,4), (3,4) for 1s; (2,5) for 3s -> 3 + 1 = 4
#
# Example 2:
# Input: nums = [1, 1, 1, 1]
# Output: 6  # 4 * 3 // 2 = 6
#
# Example 3 (Edge Case - All Distinct Negative Numbers):
# Input: nums = [-1, -2, -3]
# Output: 0  # No matching pairs

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

