# Calculate factorial of a number recursively.
# Example 1: Input: 5 -> Output: 120
# Example 2: Input: 3 -> Output: 6

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter the number: "))
if number >= 0:
    print("Factorial:", factorial(number))
else:
    print("Factorial is not defined for negative numbers")
