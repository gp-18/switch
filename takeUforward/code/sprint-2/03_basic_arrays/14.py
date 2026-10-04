# Sum of Elements at Odd Indices
# Given an array `nums`, calculate and return the sum of elements located at odd indices (1, 3, 5, ...).
#
# Example 1:
# Input: nums = [10, 20, 30, 40, 50]
# Output: 60  # nums[1] + nums[3] = 20 + 40 = 60
#
# Example 2:
# Input: nums = [5, 15, 25, 35]
# Output: 50  # nums[1] + nums[3] = 15 + 35 = 50
#
# Example 3 (Edge Case - Single Element / Negative Elements):
# Input: nums = [100]
# Output: 0  # No odd indices exist

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

