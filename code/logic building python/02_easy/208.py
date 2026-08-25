# Write a recursive factorial function.
# Example 1: Input: 5 -> Output: 120
# Example 2: Input: 4 -> Output: 24

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

number = int(input("Enter number: "))
if number >= 0:
    print("Factorial:", factorial(number))
else:
    print("Number must be non-negative")
