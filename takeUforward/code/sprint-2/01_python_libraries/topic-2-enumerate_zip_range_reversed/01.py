# Given a list of numbers, print each index and value using enumerate().

# Example 1:
# Input: nums = [10, 20, 30]
# Output: 0: 10, 1: 20, 2: 30

# Example 2:
# Input: nums = [5, 15]
# Output: 0: 5, 1: 15

nums = [10, 20, 30]
for idx, val in enumerate(nums):
    print(f"{idx}: {val}")
