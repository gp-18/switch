# Sort a list in-place and compare the result with sorted().

# Example 1:
# Input: nums = [3, 1, 2]; nums.sort()
# Output: nums is modified in-place to [1, 2, 3]

# Example 2:
# Input: nums = [3, 1, 2]; new_list = sorted(nums)
# Output: new_list is [1, 2, 3], original nums remains [3, 1, 2]

nums = [3, 1, 2]
new_list = sorted(nums)
print(f"new_list = {new_list}, original nums = {nums}")

nums.sort()
print(f"in-place sort: {nums}")
