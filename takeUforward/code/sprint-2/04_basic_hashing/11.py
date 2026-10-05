# First Repeating Element in Array
# Given an array `nums`, find and return the first element that repeats (the one whose first occurrence has the smallest index and appears again later). Return -1 if no element repeats.
#
# Example 1:
# Input: nums = [10, 5, 3, 4, 3, 5, 6]
# Output: 5  # 5 repeats and appears before 3 repeats
#
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: -1  # No repeating elements
#
# Example 3 (Edge Case - Repeating Negative Element):
# Input: nums = [-1, -2, -3, -2, -1]
# Output: -1  # -1 is the first element that repeats

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

freq = {}

for value in array:
    freq[value] = freq.get(value, 0) + 1

for value in array:
    if freq[value] > 1:
        print(f"The first repeating element is : {value}")
        break
else:
    print("-1")