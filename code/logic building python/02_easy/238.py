# Find the unique number in a list where all others are identical.
# Example 1: Input: [3, 3, 3, 7, 3, 3] -> Output: 7
# Example 2: Input: [0, 0, 0.55, 0, 0] -> Output: 0.55

lst = [3, 3, 3, 7, 3, 3]

unique = [x for x in set(lst) if lst.count(x) == 1]
print("List:", lst)
print("Unique number:", unique[0] if unique else "None")
