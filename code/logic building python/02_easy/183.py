# Remove empty lists from a list of lists.
# Example 1: Input: [[1, 2], [], [3, 4], []] -> Output: [[1, 2], [3, 4]]
# Example 2: Input: [[], [5], []] -> Output: [[5]]

list_of_lists = [[1, 2], [], [3, 4], [], [], [5]]

print("Original list of lists:", list_of_lists)

# Remove empty lists using list comprehension
filtered_list = [sublist for sublist in list_of_lists if len(sublist) > 0]

print("List after removing empty lists:", filtered_list)
