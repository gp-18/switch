# For a function that divides two numbers, list and test at least four edge cases, including a zero denominator.

# Example 1:
# Normal case: divide(10, 2) -> 5.0
# Zero denominator edge case: divide(10, 0) -> "Error: Division by zero"

# Example 2:
# Negative numbers: divide(-10, 2) -> -5.0
# Zero numerator: divide(0, 5) -> 0.0

def divide(a: float, b: float):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Test edge cases:
# 1. Normal case
print(f"Normal division: divide(10, 2) -> {divide(10, 2)}")

# 2. Zero denominator edge case
print(f"Zero denominator: divide(10, 0) -> {divide(10, 0)}")

# 3. Negative numerator edge case
print(f"Negative numerator: divide(-10, 2) -> {divide(-10, 2)}")

# 4. Zero numerator edge case
print(f"Zero numerator: divide(0, 5) -> {divide(0, 5)}")

# 5. Negative denominator edge case
print(f"Negative denominator: divide(10, -2) -> {divide(10, -2)}")

# 6. Both negative numbers
print(f"Both negative: divide(-10, -2) -> {divide(-10, -2)}")
