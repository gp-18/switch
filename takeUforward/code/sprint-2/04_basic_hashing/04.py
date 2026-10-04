# Sum of Highest and Lowest Frequency
# Given an array `nums`, find the highest frequency and the lowest frequency among all distinct elements, and return their sum.
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 3, 3]
# Output: 4  # Highest freq = 3 (for 3), Lowest freq = 1 (for 1); Sum = 3 + 1 = 4
#
# Example 2:
# Input: nums = [10, 10, 20, 20, 20, 30]
# Output: 4  # Highest freq = 3, Lowest freq = 1; Sum = 3 + 1 = 4
#
# Example 3 (Edge Case - All Elements Have Identical Frequency):
# Input: nums = [5, 5, 5]
# Output: 6  # Highest freq = 3, Lowest freq = 3; Sum = 3 + 3 = 6

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

