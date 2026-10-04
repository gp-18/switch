# Count Positive, Negative and Zero Elements
# Given an array `nums` of integers, count the number of positive elements, negative elements, and zero elements.
#
# Example 1:
# Input: nums = [1, -2, 0, 4, -5, 6, 0]
# Output: {'positive': 3, 'negative': 2, 'zero': 2}
#
# Example 2:
# Input: nums = [5, 10, 15]
# Output: {'positive': 3, 'negative': 0, 'zero': 0}
#
# Example 3 (Edge Case - All Negatives and Zeros):
# Input: nums = [-1, 0, -2, 0]
# Output: {'positive': 0, 'negative': 2, 'zero': 2}

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

