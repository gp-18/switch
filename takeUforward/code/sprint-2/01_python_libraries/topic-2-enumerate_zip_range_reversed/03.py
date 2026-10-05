# Demonstrate what happens when the two lists passed to zip() have different lengths.

# Example 1:
# Input: list1 = [1, 2, 3, 4], list2 = ['a', 'b']
# Output: [(1, 'a'), (2, 'b')] (stops at the length of the shortest list)

# Example 2:
# Input: list1 = ['x'], list2 = [10, 20, 30]
# Output: [('x', 10)]

list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
result = list(zip(list1, list2))
print(result)
