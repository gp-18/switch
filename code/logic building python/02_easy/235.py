# Sort a list and remove duplicates.
# Example 1: Input: [5, 3, 1, 3, 5, 2] -> Output: [1, 2, 3, 5]
# Example 2: Input: ['b', 'a', 'b', 'c'] -> Output: ['a', 'b', 'c']

lst = [5, 3, 1, 3, 5, 2]

sorted_unique = sorted(set(lst))
print("Original list:", lst)
print("Sorted unique list:", sorted_unique)
