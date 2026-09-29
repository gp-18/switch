# Write max_of_two(a, b) without using max(), including equal values.

# Example 1:
# Input: max_of_two(10, 20)
# Output: 20

# Example 2:
# Input: max_of_two(8, 8)
# Output: 8

def max_of_two(a, b):
    if a >= b:
        return a
    else:
        return b

print(max_of_two(10, 20))
print(max_of_two(8, 8))
