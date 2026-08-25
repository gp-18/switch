# Find the missing number in a list of 1 to 10.
# Example 1: Input: [1, 2, 3, 4, 6, 7, 8, 9, 10] -> Output: 5
# Example 2: Input: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> Output: 10

nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]

expected_sum = 10 * 11 // 2
actual_sum = sum(nums)
missing_number = expected_sum - actual_sum

print("List:", nums)
print("Missing number:", missing_number)
