# Write factorial(n) for non-negative integers; decide how to handle negative input.

# Example 1:
# Input: factorial(5)
# Output: 120 (5 * 4 * 3 * 2 * 1 = 120)

# Example 2:
# Input: factorial(0)
# Output: 1

def factorial(n: int):
    if n < 0:
        return None  # Or raise ValueError("Negative numbers do not have factorials.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(0))
print(f"factorial(-3) -> {factorial(-3)} (handled: undefined for negative numbers)")
