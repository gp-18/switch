# Sum of Elements at Even Indices
# Given an array `nums`, calculate and return the sum of elements located at even indices (0, 2, 4, ...).
#
# Example 1:
# Input: nums = [10, 20, 30, 40, 50]
# Output: 90  # nums[0] + nums[2] + nums[4] = 10 + 30 + 50 = 90
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: 4  # nums[0] + nums[2] = 1 + 3 = 4
#
# Example 3 (Edge Case - Negative Elements at Even Indices):
# Input: nums = [-10, 5, -20, 15]
# Output: -30  # (-10) + (-20) = -30

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

sum_at_even_location = 0 
for i in range(0 , len(array) , 2) :
  sum_at_even_location += array[i] 

print(f"Sum of elements at even indices : {sum_at_even_location}")
