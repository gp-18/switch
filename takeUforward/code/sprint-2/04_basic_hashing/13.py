# Count Occurrences of a Given Number (Multiple Queries)
# Given an array `nums` and a list of query numbers `queries`, precompute the frequencies of all numbers in `nums` so that each query count can be answered in O(1) time.
#
# Example 1:
# Input: nums = [1, 3, 2, 1, 3, 1], queries = [1, 3, 4]
# Output: [3, 2, 0]
#
# Example 2:
# Input: nums = [10, 20, 30], queries = [10, 50]
# Output: [1, 0]
#
# Example 3 (Edge Case - Queries for Negative Numbers and Zero):
# Input: nums = [-2, 0, -2, 5], queries = [-2, 0, -5]
# Output: [2, 1, 0]

length = int(input("Enter the length of the array : "))
array = []

for i in range(0 , length) :
  value = int(input(f"Enter the value to insert at index {i} : "))
  array.append(value)

print(f"Your array has become : {array} and now doing the operations on it.")

