# Build a list using append() and extend() and explain the difference.

# Example 1:
# Input: a = [1, 2]; a.append([3, 4])
# Output: [1, 2, [3, 4]] (adds object as a single element)

# Example 2:
# Input: a = [1, 2]; a.extend([3, 4])
# Output: [1, 2, 3, 4] (iterates and appends each element)

a = [1, 2]
a.append([3, 4])
print(f"append: {a}")

b = [1, 2]
b.extend([3, 4])
print(f"extend: {b}")
