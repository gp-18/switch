# Filter a list to return only non-negative integers.
# Example 1: Input: [1, -2, 3, -4, 5, 0] -> Output: [1, 3, 5, 0]
# Example 2: Input: [-10, 20, -30, 40] -> Output: [20, 40]

numbers = [1, -2, 3, -4, 5, 0]

non_negative = [x for x in numbers if x >= 0]
print("Original list:", numbers)
print("Non-negative integers:", non_negative)
