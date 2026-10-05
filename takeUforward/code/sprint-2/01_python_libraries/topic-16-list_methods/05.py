# Create a shallow copy of a list and demonstrate what copying means.

# Example 1:
# Input: a = [1, [2, 3]]; b = a.copy(); a[0] = 99
# Output: a[0] is 99, but b[0] remains 1

# Example 2:
# Input: a = [1, [2, 3]]; b = a.copy(); a[1].append(4)
# Output: b[1] becomes [2, 3, 4] (inner mutable object is shared)

a = [1, [2, 3]]
b = a.copy()
a[0] = 99
print(f"a[0] = {a[0]}, b[0] = {b[0]}")
a[1].append(4)
print(f"b[1] = {b[1]}")
