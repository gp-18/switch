# Remove values using both remove() and pop() and explain their differences.

# Example 1:
# Input: a = [10, 20, 30, 20]; a.remove(20)
# Output: [10, 30, 20] (removes first matching value)

# Example 2:
# Input: a = [10, 20, 30]; val = a.pop(1)
# Output: val = 20, a = [10, 30] (removes and returns item at index)

a = [10, 20, 30, 20]
a.remove(20)
print(f"After remove(20): {a}")

val = a.pop(1)
print(f"val = {val}, a = {a}")
