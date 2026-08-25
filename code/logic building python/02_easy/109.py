# Find sum of digits of a number recursively.
# Example 1: Input: 1234 -> Output: 10
# Example 2: Input: 456 -> Output: 15

def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

number = int(input("Enter the number: "))
if number >= 0:
    print("Sum of digits:", sum_of_digits(number))
else:
    print("Please enter a non-negative integer")
