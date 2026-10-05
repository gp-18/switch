# Missing Number
# Given an array `nums` containing `n` distinct numbers taken from the range `[0, n]`, use a hash set or boolean frequency array to find the single number missing from the range.
#
# Example 1:
# Input: nums = [3, 0, 1]
# Output: 2  # n = 3, range [0, 3], missing is 2
#
# Example 2:
# Input: nums = [0, 1]
# Output: 2  # n = 2, range [0, 2], missing is 2
#
# Example 3 (Edge Case - Missing Zero):
# Input: nums = [1, 2, 3]
# Output: 0  # n = 3, range [0, 3], missing is 0

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")
num_set = set(array)
n = len(array)
missing_number = -1

for i in range(n + 1):
    if i not in num_set:
        missing_number = i
        break

print(f"The missing number is : {missing_number}")
