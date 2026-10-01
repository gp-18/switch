# Swap the values of two variables without creating a third variable.

# Example 1:
# Input: a = 10, b = 20
# Output:
# Before swapping: a = 10, b = 20
# After swapping: a = 20, b = 10

# Example 2:
# Input: a = "cat", b = "dog"
# Output:
# Before swapping: a = cat, b = dog
# After swapping: a = dog, b = cat

a, b = 10, 20
print("Before swapping: a =", a, ", b =", b)
a, b = b, a
print("After swapping: a =", a, ", b =", b)
