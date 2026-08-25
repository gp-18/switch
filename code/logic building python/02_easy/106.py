# Calculate power of a number (x^n) using recursion.
# Example 1: Input: x=2, n=3 -> Output: 8
# Example 2: Input: x=5, n=2 -> Output: 25

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

base = float(input("Enter the base x: "))
exp = int(input("Enter the exponent n: "))
if exp >= 0:
    print("Result:", power(base, exp))
else:
    print("Please enter a non-negative exponent")
