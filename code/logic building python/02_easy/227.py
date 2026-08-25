# Return only integers from a mixed list (exclude booleans).
# Example 1: Input: [10, 'hello', True, 20, False] -> Output: [10, 20]
# Example 2: Input: [False, 100, 'python', 200] -> Output: [100, 200]

items = [10, "hello", True, 20, False, 30.5]

integers = [x for x in items if type(x) == int]
print("Original list:", items)
print("Integers only:", integers)
