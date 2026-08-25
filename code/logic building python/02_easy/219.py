# Filter a mixed list to return only integers.
# Example 1: Input: [1, 2, 'a', 'b', True, False, 3] -> Output: [1, 2, 3]
# Example 2: Input: ['x', 10, True, 20.5, 30] -> Output: [10, 30]

mixed_list = [1, 2, "a", "b", True, False, 3, 4.5]

# Note: type(x) == int excludes booleans since bool is a subclass of int
integers_only = [x for x in mixed_list if type(x) == int]
print("Mixed list:", mixed_list)
print("Integers only:", integers_only)
