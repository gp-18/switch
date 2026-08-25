# Check if a number is symmetrical (same as its reverse).
# Example 1: Input: 121 -> Output: Symmetrical
# Example 2: Input: 123 -> Output: Not symmetrical

number = input("Enter a number: ")

if number == number[::-1]:
    print("Symmetrical number")
else:
    print("Not symmetrical")
