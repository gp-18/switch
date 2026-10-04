# Count Elements That Appear More Than Once
# Given an array `nums`, count and return how many distinct elements have a frequency greater than 1 (i.e. duplicates).
#
# Example 1:
# Input: nums = [1, 2, 2, 3, 4, 4, 4, 5]
# Output: 2  # Elements appearing >1 time: 2, 4
#
# Example 2:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 0  # All elements are unique
#
# Example 3 (Edge Case - All Identical Negative Elements):
# Input: nums = [-3, -3, -3]
# Output: 1  # Element -3 appears >1 time

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

