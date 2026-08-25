# Add each element's index to itself in a list.
# Example 1: Input: [0, 0, 0, 0, 0] -> Output: [0, 1, 2, 3, 4]
# Example 2: Input: [1, 2, 3, 4, 5] -> Output: [1, 3, 5, 7, 9]

lst = [1, 2, 3, 4, 5]

result = [i + val for i, val in enumerate(lst)]
print("Original list:", lst)
print("List after adding index:", result)
