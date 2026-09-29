# Write power(base, exponent=2) and test both the default and custom exponent.

# Example 1:
# Input: power(3)
# Output: 9 (3^2 = 9, default exponent=2)

# Example 2:
# Input: power(2, 4)
# Output: 16 (2^4 = 16, custom exponent=4)

def power(base: float, exponent: float = 2) -> float:
    return base ** exponent

# Test default exponent
print(power(3))

# Test custom exponent
print(power(2, 4))
