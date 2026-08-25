# Create a binary representation of a decimal number (return as string).
# Example 1: Input: 10 -> Output: '1010'
# Example 2: Input: 5 -> Output: '101'

number = int(input("Enter a decimal number: "))
if number >= 0:
    binary_str = bin(number)[2:]
    print("Binary representation:", binary_str)
else:
    print("Please enter a non-negative integer")
