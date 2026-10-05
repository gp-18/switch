# Use reduce() to calculate the product of a list.

# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: reduce(lambda a, b: a * b, nums) -> 24

# Example 2:
# Input: nums = [2, 5, 10]
# Output: 100

from functools import reduce

nums = [1, 2, 3, 4]
prod = reduce(lambda a, b: a * b, nums)
print(prod)
